# บทบาทและเป้าหมายหลัก (System Identity & Mission)
คุณทำหน้าที่เป็น Software Architect, Systems Engineer และ Code Optimization Agent ระดับองค์กร[span_2](start_span)[span_2](end_span) เป้าหมายสูงสุดของคุณคือการพัฒนาและปรับปรุงระบบให้ทำงานถูกต้องตามวัตถุประสงค์ รักษาสถาปัตยกรรมที่พิสูจน์แล้วว่าใช้งานได้ และมุ่งสู่ผลลัพธ์แบบ "Zero Known Defects" หรือไร้ข้อผิดพลาดโดยสิ้นเชิง ณ จุดส่งมอบ[span_3](start_span)[span_3](end_span) 

กรุณารักษาน้ำเสียงที่เป็นบวก อดทน และให้การสนับสนุนอย่างเต็มที่เสมอ ใช้ภาษาที่สุภาพ เป็นทางการ และอธิบายการทำงานให้เข้าใจง่าย

# 1. ปรัชญาการทำงาน (Prime Directive)
* **Preserve Before Replace:** โค้ดเดิมที่ทำงานได้ถูกต้องถือเป็นแหล่งอ้างอิงหลัก ห้ามลบ รื้อ หรือเขียนระบบใหม่ทั้งหมดเพียงเพราะมีวิธีใหม่กว่า หากไม่มีเหตุผลด้านความปลอดภัยหรือข้อจำกัดที่ชัดเจน[span_4](start_span)[span_4](end_span)
* **Zero-Defect Refactoring:** ทุกการปรับปรุงโค้ดต้องปราศจากบั๊ก (Bug-free) และต้องไม่มีการแจ้งเตือน (Zero Warnings) ใดๆ ข้ามผ่านกระบวนการคอมไพล์
* **Strict Modification Protocols:** ต้องวิเคราะห์และทำความเข้าใจโครงสร้าง การไหลเวียนของข้อมูล (Data flow) และผลกระทบต่อระบบส่วนอื่นๆ อย่างถี่ถ้วนก่อนทำการแก้ไขใดๆ[span_5](start_span)[span_5](end_span)

# 2. กฎและข้อบังคับในการส่งมอบงาน (Strict Execution & Delivery Rules)
* **1. การส่งมอบโค้ดฉบับสมบูรณ์ (Full File Delivery):** หากมีการสั่งให้เขียน แก้ไข หรือปรับปรุงโค้ด **คุณต้องส่งมอบไฟล์โค้ดฉบับเต็มและสมบูรณ์เสมอ** ห้ามส่งมอบเพียงบางส่วน (Snippets) หรือละเว้นโค้ดส่วนเดิม และต้องส่งมอบให้ครบตามจำนวนไฟล์ที่เกี่ยวข้องทั้งหมด
* **2. การออกแบบระบบอัตโนมัติ (Batch Automation):** ทุกครั้งที่มีการสร้างสคริปต์ `.bat` จะต้องออกแบบให้สามารถ "ลากแล้ววาง" (Drag-and-Drop) โฟลเดอร์เป้าหมายเข้าไปเพื่อดำเนินการต่อได้ทันที และต้องตั้งค่าให้คำสั่งระบบรวมถึงผลลัพธ์ในหน้า Terminal แสดงผลเป็นภาษาอังกฤษทั้งหมด
* **3. การกำหนดเส้นทาง Python:** สำหรับเครื่องมือที่รันผ่าน Python ให้บังคับใช้เส้นทางเริ่มต้นที่ `B:\Thai RVC WebUI\runtime\python.exe` เสมอ
* **4. อินเทอร์เฟซสองภาษา (Bilingual UI):** การพัฒนาและปรับปรุงส่วนต่อประสานกับผู้ใช้ (UI) ต้องรองรับการแสดงผลทั้งภาษาไทยและภาษาอังกฤษอย่างสม่ำเสมอ
* **5. การให้เครดิต (Credit & Ownership):** ทุกครั้งที่มีการสร้างหรือปรับปรุงไฟล์โค้ด ให้ใส่ข้อความให้เครดิตไว้ในโค้ดเสมอ โดยใช้รูปแบบ: 
  `Made And Checked By DELTA SYNTH & Gemini AI` 
  ตามด้วย `Original by [ชื่อเจ้าของต้นฉบับ]` เรียงตามลำดับ[span_6](start_span)[span_6](end_span)

# 3. กระบวนการทำงานที่เป็นระบบ (Standard Workflow)
คุณต้องดำเนินงานตามขั้นตอนต่อไปนี้อย่างเคร่งครัด[span_7](start_span)[span_7](end_span):
* **ANALYZE:** ตรวจสอบโครงสร้างไฟล์ ค้นหาสาเหตุที่แท้จริงของปัญหา (Root Cause) และแยกแยะออกจากอาการที่แสดงผล[span_8](start_span)[span_8](end_span)
* **PLAN:** วางแผนโดยเลือกใช้การเปลี่ยนแปลงที่ปลอดภัยที่สุด (Smallest Safe Change) เพื่อรักษาพฤติกรรมหลักที่ถูกต้องของระบบเดิมไว้[span_9](start_span)[span_9](end_span)
* **EXECUTE:** ดำเนินการแก้ไขที่ต้นเหตุ ไม่สร้างแพตช์ซ้อนทับ รักษาโครงสร้างการตั้งชื่อ และหลีกเลี่ยงการสร้างตรรกะที่ซ้ำซ้อน[span_10](start_span)[span_10](end_span)
* **VERIFY:** ทดสอบความถูกต้อง ตรวจสอบผลลัพธ์ ครอบคลุมถึงกรณีข้อมูลผิดพลาด (Edge cases) และประเมินการใช้ทรัพยากร (CPU, RAM, GPU) อย่างรัดกุม[span_11](start_span)[span_11](end_span)

# 4. สรุปผลการทำงาน (Post-Work Report)
ทุกครั้งที่การแก้ไขเสร็จสิ้น ให้สรุปผลลัพธ์การทำงานอย่างกระชับ โดยแบ่งเป็นหัวข้อดังนี้[span_12](start_span)[span_12](end_span):
* **[Files Changed]:** ระบุไฟล์ที่ได้รับการแก้ไข
* **[Logic Altered]:** ระบุตรรกะที่ถูกเปลี่ยนแปลง เหตุผล และพฤติกรรมเดิมที่ยังคงรักษาไว้
* **[Performance Impact]:** ระบุผลกระทบต่อทรัพยากรและความเสถียรของระบบ
* **[Residual Risks]:** ระบุความเสี่ยงที่อาจหลงเหลืออยู่ หากไม่มีให้ระบุว่า `none known`
	</tr>
</table>

## 简介
本仓库具有以下特点
+ 使用top1检索替换输入源特征为训练集特征来杜绝音色泄漏
+ 即便在相对较差的显卡上也能快速训练
+ 使用少量数据进行训练也能得到较好结果(推荐至少收集10分钟低底噪语音数据)
+ 可以通过模型融合来改变音色(借助ckpt处理选项卡中的ckpt-merge)
+ 简单易用的网页界面
+ 可调用pymss/MSST模型来快速分离人声和伴奏
+ 使用最先进的[人声音高提取算法InterSpeech2023-RMVPE](#参考项目)根绝哑音问题，速度快、资源占用小
+ A卡/I卡使用 CPU 依赖方案；Windows 可使用 DirectML，Linux 使用 CPU

点此查看我们的[演示视频](https://www.bilibili.com/video/BV1pm4y1z7Gm/) !

## 环境配置

本分支面向 **Python 3.12 x64**，请先进入仓库根目录。Ubuntu 推荐使用 Ubuntu 24.04 x86_64。

### Ubuntu 24.04

```bash
sudo apt update
sudo apt install -y python3.12 python3.12-venv python3.12-dev ffmpeg unzip libsndfile1 libportaudio2

python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
```

### Windows

安装 Python 3.12 x64 后创建虚拟环境：

```powershell
py -3.12 -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip setuptools wheel
```

### 按硬件选择依赖

| 硬件 | 安装方式 |
| --- | --- |
| CPU、AMD、Intel | 使用 `requirments_cpu_py312.txt`；Windows 可使用 DirectML，Linux 使用 CPU |
| NVIDIA RTX 50 系 | 先安装 CUDA 12.8 版 Torch，再安装 `requirments_cu128_py312.txt` |
| NVIDIA RTX 50 系以前 | 先安装 CUDA 11.8 版 Torch，再安装 `requirments_cu118_py312.txt` |

#### CPU、AMD、Intel

```bash
python -m pip install -r requirments_cpu_py312.txt
```

#### NVIDIA RTX 50 系：两阶段安装

```bash
python -m pip install torch==2.7.1+cu128 torchaudio==2.7.1+cu128 \
  --index-url https://download.pytorch.org/whl/cu128 \
  --extra-index-url https://pypi.org/simple
python -m pip install -r requirments_cu128_py312.txt
```

#### NVIDIA RTX 50 系以前：两阶段安装

```bash
python -m pip install torch==2.7.1+cu118 torchaudio==2.7.1+cu118 \
  --index-url https://download.pytorch.org/whl/cu118 \
  --extra-index-url https://pypi.org/simple
python -m pip install -r requirments_cu118_py312.txt
```

检查 Torch 与 CUDA 状态：

```bash
python -c "import torch; print('torch:', torch.__version__); print('cuda:', torch.version.cuda); print('cuda available:', torch.cuda.is_available())"
```


### 修改下载源

三个 `requirments_*.txt` 顶部已经包含下载源。中国大陆用户可保留默认镜像；需要使用官方源时，只替换 `--index-url` 和 `--extra-index-url`，保留包版本、CUDA 后缀和两阶段顺序。

| Default mirror | Official source |
| --- | --- |
| `https://mirrors.pku.edu.cn/pypi/simple` | `https://pypi.org/simple` |
| `https://mirrors.nju.edu.cn/pytorch/whl/cpu` | `https://download.pytorch.org/whl/cpu` |
| `https://mirrors.nju.edu.cn/pytorch/whl/cu118` | `https://download.pytorch.org/whl/cu118` |
| `https://mirrors.nju.edu.cn/pytorch/whl/cu128` | `https://download.pytorch.org/whl/cu128` |

## 模型与运行目录

WebUI 会自动创建运行目录。模型请从 [Hugging Face 模型仓库](https://huggingface.co/lj1995/VoiceConversionWebUI/tree/main) 下载，并保持以下路径：

```text
assets/
├── hubert_base/
│   ├── config.json
│   ├── preprocessor_config.json
│   └── pytorch_model.bin
├── rmvpe/rmvpe.pt
├── pretrained/
├── pretrained_v2/
├── pymss_weights/
├── weights/        # user RVC .pth models
└── indices/        # user .index files
logs/
└── mute/           # training silence samples

# Exact paths used by the code
assets/hubert_base/config.json
assets/hubert_base/preprocessor_config.json
assets/hubert_base/pytorch_model.bin
assets/rmvpe/rmvpe.pt
assets/pretrained/*.pth
assets/pretrained_v2/*.pth
assets/pymss_weights/*
assets/weights/*.pth
assets/indices/*.index
logs/mute/*
```

### 下载模型

```bash
python -m pip install --upgrade huggingface_hub

# Required for inference and feature extraction
hf download lj1995/VoiceConversionWebUI --revision main \
  --include "hubert_base/*" --local-dir assets
hf download lj1995/VoiceConversionWebUI rmvpe.pt --revision main \
  --local-dir assets/rmvpe

# Required for v1/v2 training
hf download lj1995/VoiceConversionWebUI --revision main \
  --include "pretrained/*" "pretrained_v2/*" --local-dir assets
hf download lj1995/VoiceConversionWebUI mute.zip --revision main \
  --local-dir .model-downloads
python -m zipfile -e .model-downloads/mute.zip logs

# Required only for pymss/MSST vocal separation
hf download lj1995/VoiceConversionWebUI --revision main \
  --include "pymss_weights/*" --local-dir assets
```

仅 Windows AMD/Intel DirectML 环境还需要：

```bash
hf download lj1995/VoiceConversionWebUI rmvpe.onnx --revision main \
  --local-dir assets/rmvpe
```

### FFmpeg

Ubuntu 已在前面的系统依赖命令中安装 FFmpeg。Windows 用户可把下面两个文件放到项目根目录：

- [ffmpeg.exe](https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/ffmpeg.exe?download=true)
- [ffprobe.exe](https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/ffprobe.exe?download=true)

## 开始使用

启动 WebUI：

```bash
python webui.py
```

无桌面的 Ubuntu 服务器：

```bash
python webui.py --noautoopen
```

默认服务监听端口为 `7865`。用户自己的 `.pth` 模型放入 `assets/weights/`，`.index` 文件放入 `assets/indices/`。

## 参考项目
+ [ContentVec](https://github.com/auspicious3000/contentvec/)
+ [VITS](https://github.com/jaywalnut310/vits)
+ [HIFIGAN](https://github.com/jik876/hifi-gan)
+ [Gradio](https://github.com/gradio-app/gradio)
+ [FFmpeg](https://github.com/FFmpeg/FFmpeg)
+ [Ultimate Vocal Remover](https://github.com/Anjok07/ultimatevocalremovergui)
+ [pymss-project/pymss](https://github.com/pymss-project/pymss)
+ [audio-slicer](https://github.com/openvpi/audio-slicer)
+ [Vocal pitch extraction:RMVPE](https://github.com/Dream-High/RMVPE)
  + The pretrained model is trained and tested by [yxlllc](https://github.com/yxlllc/RMVPE) and [RVC-Boss](https://github.com/RVC-Boss).

## 感谢所有贡献者作出的努力
<a href="https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/graphs/contributors" target="_blank">
  <img src="https://contrib.rocks/image?repo=RVC-Project/Retrieval-based-Voice-Conversion-WebUI" />
</a>
