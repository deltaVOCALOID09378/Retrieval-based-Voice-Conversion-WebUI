# -*- coding: utf-8 -*-
# ==========================================
# Made and Checked By DELTA SYNTH And Gemini Claude and ChatGPT
# Original By Patiphat Wongyai (Delta) & RVC Project
# File: tabs/faq.py | Version: 1.0
# ==========================================

import gradio as gr
import traceback

def render_tab_faq():
    """
    ฟังก์ชันสำหรับเรนเดอร์แท็บ 'คำถามที่พบบ่อย (FAQ)'
    ทำหน้าที่แสดงผลไฟล์ Markdown ที่เก็บข้อมูลคำถามและการแก้ไขปัญหาเบื้องต้น
    """
    # ประกาศค่าตัวแปรหัวข้อแท็บ เพื่อป้องกันการเกิด NameError เมื่อรันหน้าต่าง UI
    tab_faq = "คำถามที่พบบ่อย (FAQ)"
    
    with gr.TabItem(tab_faq):
        try:
            # อ่านไฟล์อธิบายข้อมูลจากโฟลเดอร์ docs ด้วยการเข้ารหัส utf8
            with open("docs/en/faq_en.md", "r", encoding="utf8") as f:
                info = f.read()
            gr.Markdown(value=info)
        except Exception:
            # หากไม่พบไฟล์หรือมีปัญหาในการอ่าน จะแสดงข้อผิดพลาดออกมาเพื่อให้ทราบถึงสาเหตุ
            gr.Markdown(traceback.format_exc())