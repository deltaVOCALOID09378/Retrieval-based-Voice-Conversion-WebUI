# -*- coding: utf-8 -*-
# ==========================================
# File: infer-web.py | Version: 2.5
# Made and Checked By DELTA SYNTH And Gemini Claude and ChatGPT
# Original By Patiphat Wongyai (Delta) & RVC Project
# Date: 2026-08-05
# Update v2.5: 
#  - Enforced absolute path for Python executable to ensure stability across subprocesses.
#  - Standardized headers and credit formats.
# ==========================================

import os
import sys
import shutil
import logging
import traceback
import torch
import platform
import numpy as np
import gradio as gr
import faiss
import fairseq
import pathlib
import json
from time import sleep
from subprocess import Popen
from random import shuffle
import warnings
import threading
import soundfile as sf
from dotenv import load_dotenv

now_dir = os.getcwd()
sys.path.append(now_dir)
load_dotenv()

from infer.modules.vc.modules import VC
from infer.modules.uvr5.modules import uvr
from infer.lib.train.process_ckpt import change_info, extract_small_model, merge, show_info
from i18n.i18n import I18nAuto
from configs.config import Config
from sklearn.cluster import MiniBatchKMeans

# ==========================================
# PyTorch 2.6+ Safe Globals Fix
# ==========================================
try:
    from fairseq.data.dictionary import Dictionary
    if hasattr(torch.serialization, 'add_safe_globals'):
        torch.serialization.add_safe_globals([Dictionary])
except Exception as e:
    logging.warning(f"Could not register safe globals for fairseq: {e}")

logging.getLogger("numba").setLevel(logging.ERROR)
logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("gradio").setLevel(logging.ERROR)
logger = logging.getLogger(__name__)
warnings.filterwarnings("ignore")
torch.manual_seed(114514)

tmp = os.path.join(now_dir, "TEMP")
shutil.rmtree(tmp, ignore_errors=True)
shutil.rmtree("%s/runtime/Lib/site-packages/infer_pack" % (now_dir), ignore_errors=True)
shutil.rmtree("%s/runtime/Lib/site-packages/uvr5_pack" % (now_dir), ignore_errors=True)
os.makedirs(tmp, exist_ok=True)
os.makedirs(os.path.join(now_dir, "logs"), exist_ok=True)
os.makedirs(os.path.join(now_dir, "assets/weights"), exist_ok=True)
os.environ["TEMP"] = tmp

config = Config()
vc = VC(config)

if config.dml == True:
    def forward_dml(ctx, x, scale):
        ctx.scale = scale
        res = x.clone().detach()
        return res
    fairseq.modules.grad_multiply.GradMultiply.forward = forward_dml

i18n = I18nAuto()
logger.info(i18n)

ngpu = torch.cuda.device_count()
gpu_infos = []
mem = []
if_gpu_ok = False

if torch.cuda.is_available() or ngpu != 0:
    for i in range(ngpu):
        gpu_name = torch.cuda.get_device_name(i)
        if_gpu_ok = True
        gpu_infos.append(f"GPU {i}\t{gpu_name}")
        mem.append(int(torch.cuda.get_device_properties(i).total_memory / 1024 / 1024 / 1024 + 0.4))
        
if if_gpu_ok and len(gpu_infos) > 0:
    gpu_info = "ตรวจพบกราฟิกการ์ด (GPU Detected):\n" + "\n".join(gpu_infos)
    default_batch_size = max(1, min(mem) // 2)
elif config.dml == True:
    gpu_info = "ทำงานด้วยระบบ DirectML สำหรับ DirectX (Operating via DirectML for DirectX)"
    default_batch_size = 1
else:
    gpu_info = "ทำงานด้วยระบบหน่วยประมวลผลกลาง / อุปกรณ์ภายนอก (Operating via CPU / External USB Unit)"
    default_batch_size = 1

gpus = "-".join([i[0] for i in gpu_infos]) if if_gpu_ok else ""
logger.info(gpu_info)

weight_root = os.getenv("weight_root", "assets/weights")
weight_uvr5_root = os.getenv("weight_uvr5_root", "assets/uvr5_weights")
index_root = os.getenv("index_root", "logs")

base_source_dir = os.path.join(now_dir, "For OpenUtau VB Making", "A Voicebank File")
SOURCE_DIRS = {
    "1. EN": os.path.join(base_source_dir, "EN"),
    "2. TH": os.path.join(base_source_dir, "TH"),
    "3. JP": os.path.join(base_source_dir, "JP")
}
VOICEBANK_FORMATS = {
    "EN": "English Arpasing",
    "TH": "Thai VCCV",
    "JP": "JPN VCV"
}

names = [name for name in os.listdir(weight_root) if name.endswith(".pth")] if os.path.exists(weight_root) else []
index_paths = []
if os.path.exists(index_root):
    for root, dirs, files in os.walk(index_root, topdown=False):
        for name in files:
            if name.endswith(".index") and "trained" not in name:
                index_paths.append("%s/%s" % (root, name))
uvr5_names = [name.replace(".pth", "") for name in os.listdir(weight_uvr5_root) if name.endswith(".pth") or "onnx" in name] if os.path.exists(weight_uvr5_root) else []

# ... [ฟังก์ชันตัวช่วยอื่นๆ ยังคงเดิมเพื่อรักษาเสถียรภาพตามต้นฉบับ] ...

    def run_subprocess_yield(cmd_args, env, cwd):
        process = Popen(cmd_args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, env=env, cwd=cwd)
        for line in process.stdout:
            yield line
        process.wait()
        if process.returncode != 0:
            yield f"Process failed with exit code {process.returncode}"
        else:
            yield "ดำเนินการเสร็จสิ้น (Finished successfully)"

    def get_ds_env():
        env = os.environ.copy()
        if config.device == "dml":
            env["CUDA_VISIBLE_DEVICES"] = "-1"
            env["PL_TORCH_DISTRIBUTED_BACKEND"] = "gloo"
        elif config.device.startswith("cuda"):
            env["CUDA_VISIBLE_DEVICES"] = config.device.split(":")[1] if ":" in config.device else "0"
        else:
            env["CUDA_VISIBLE_DEVICES"] = "-1"
        return env

    def run_diffsinger_data_prep(data_in, data_out):
        yield "เริ่มตรวจสอบและล้างข้อมูลอัตโนมัติ (Data Autocleaning)..."
        try:
            cwd = os.path.join(now_dir, "DiffSinger_Training")
            # อัปเดตและล็อกเส้นทางเพื่อเสถียรภาพ
            python_exe = r"B:\Thai RVC WebUI\runtime\python.exe"
            
            env = get_ds_env()
            yield "Running autoclean.py..."
            for line in run_subprocess_yield([python_exe, "autoclean.py", data_in], env, cwd):
                yield line
                
            yield f"\nการจัดเตรียมข้อมูลเริ่มทำ Binarization... (Output: {data_out})"
            for line in run_subprocess_yield([python_exe, "scripts/binarize.py", "--config", "configs/acoustic.yaml"], env, cwd):
                yield line
                
        except Exception as e:
            yield f"เกิดข้อผิดพลาด: {e}"

    def run_diffsinger_train(config_yaml):
        yield f"กำลังเริ่มต้นฝึกสอนด้วย {config_yaml} บนฮาร์ดแวร์ {config.device}..."
        try:
            cwd = os.path.join(now_dir, "DiffSinger_Training")
            # อัปเดตและล็อกเส้นทางเพื่อเสถียรภาพ
            python_exe = r"B:\Thai RVC WebUI\runtime\python.exe"
            env = get_ds_env()
            
            for line in run_subprocess_yield([python_exe, "scripts/train.py", "--config", config_yaml], env, cwd):
                yield line
                
        except Exception as e:
            yield f"เกิดข้อผิดพลาด: {e}"
            
    # ... [โค้ดส่วน UI ของ Gradio และการเรียก Launch คิว ยังคงเดิม] ...