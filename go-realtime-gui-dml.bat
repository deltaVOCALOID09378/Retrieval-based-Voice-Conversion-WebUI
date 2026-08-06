:: ==========================================
:: File: go-realtime-gui-dml.bat | Version: 1.0
:: Made and Checked By DELTA SYNTH And Gemini Claude and ChatGPT
:: Original By RVC Project
:: ==========================================
@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo [INFO] Starting Realtime GUI (DirectML Mode)...

"B:\Thai RVC WebUI\runtime\python.exe" gui_v1.py --pycmd "B:\Thai RVC WebUI\runtime\python.exe" --dml
pause