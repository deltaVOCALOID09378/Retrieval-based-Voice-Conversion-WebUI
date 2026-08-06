:: ==========================================
:: File: go-realtime-gui.bat | Version: 1.0
:: Made and Checked By DELTA SYNTH And Gemini Claude and ChatGPT
:: Original By RVC Project
:: ==========================================
@echo off
chcp 65001 >nul
cd /d "%~dp0"

:: Inform user about the process
echo [INFO] Starting Realtime GUI...

:: Execute GUI script securely
"B:\Thai RVC WebUI\runtime\python.exe" gui_v1.py
pause