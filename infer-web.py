# -*- coding: utf-8 -*-
# ==========================================
# Made and Checked By DELTA SYNTH And Gemini Claude and ChatGPT
# Original By Patiphat Wongyai (Delta) & RVC Project
# File: infer-web.py | Version: 2.5
# ==========================================

import gradio as gr
from core_logic import *
import traceback

# นำเข้าโมดูลแท็บต่างๆ ทั้งหมดเพื่อแยกการทำงานให้เป็นระเบียบ (Modular UI Architecture)
from tabs.uvr5 import render_tab_uvr5
from tabs.training import render_tab_training
from tabs.inference import render_tab_inference
from tabs.ckpt_processing import render_tab_ckpt_processing
from tabs.onnx_export import render_tab_onnx_export
from tabs.openutau_packager import render_tab_openutau_packager
from tabs.openutau_studio import render_tab_openutau_studio
from tabs.diffsinger_variance import render_tab_diffsinger_variance
from tabs.diffsinger_studio import render_tab_diffsinger_studio
from tabs.faq import render_tab_faq

# สร้างโครงสร้างหลักของแอปพลิเคชัน Gradio โดยรวบรวมฟังก์ชันการทำงานทั้งหมดเข้าด้วยกัน
with gr.Blocks(title='RVC WebUI for OpenUtau Voicebank (by DELTA SYNTH)') as app:
    gr.Markdown('## RVC WebUI Modularized')
    
    # รวบรวมแท็บการทำงานต่างๆ เข้าด้วยกันเพื่อสร้างหน้าต่างสำหรับให้ผู้ใช้เลือกใช้งาน
    with gr.Tabs():
        render_tab_uvr5()
        render_tab_training()
        render_tab_inference()
        render_tab_ckpt_processing()
        render_tab_onnx_export()
        render_tab_openutau_packager()
        render_tab_openutau_studio()
        render_tab_diffsinger_variance()
        render_tab_diffsinger_studio()
        render_tab_faq()
        
    # ตรวจสอบขีดจำกัดการใช้คิวจากจำนวนคอร์ของซีพียู และจำกัดปริมาณโหลดเพื่อรักษาประสิทธิภาพ (Resource Optimization)
    queue_concurrency, queue_size = webui_queue_limits(config.n_cpu)
    
    if config.iscolab:
        # เปิดให้แชร์ลิงก์สู่สาธารณะหากตรวจพบว่าทำงานอยู่บนระบบ Google Colab
        app.queue(concurrency_count=queue_concurrency, max_size=queue_size).launch(share=True)
    else:
        try:
            # เริ่มต้นรันเซิร์ฟเวอร์บนเครื่องพื้นที่ (Local) ปกติผ่าน 0.0.0.0
            app.queue(concurrency_count=queue_concurrency, max_size=queue_size).launch(
                server_name="0.0.0.0",
                inbrowser=not config.noautoopen,
                server_port=config.listen_port,
                quiet=True,
                share=True,
            )
        except ValueError as e:
            # การจัดการข้อผิดพลาด (Fallback Recovery) เมื่อเครือข่ายไม่อนุญาตให้เชื่อม 0.0.0.0 จะเปลี่ยนไปใช้ 127.0.0.1 แทนอย่างเงียบๆ
            if "localhost is not accessible" in str(e):
                logger.warning("⚠️ ไม่สามารถใช้ 0.0.0.0 ได้ (Network issue) ระบบกำลังเปลี่ยนไปใช้ 127.0.0.1 แทน...")
                app.queue(concurrency_count=queue_concurrency, max_size=queue_size).launch(
                    server_name="127.0.0.1",
                    inbrowser=not config.noautoopen,
                    server_port=config.listen_port,
                    quiet=True,
                    share=True,
                )
            else:
                raise e