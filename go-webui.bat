:: ==========================================
:: File: go-webui.bat | Version: 1.1
:: Made and Checked By DELTA SYNTH And Gemini Claude and ChatGPT
:: Original By RVC Project
:: ==========================================
@echo off
chcp 65001 >nul

:: [NOTE] Set script directory and ensure the environment variables are correctly mapped.
set "SCRIPT_DIR=%~dp0"
set "SCRIPT_DIR=%SCRIPT_DIR:~0,-1%"
cd /d "%SCRIPT_DIR%"
set "PATH=%SCRIPT_DIR%\runtime;%PATH%"
set "GRADIO_ANALYTICS_ENABLED=False"
set "NO_PROXY=localhost,127.0.0.1,::1,%NO_PROXY%"

:: [NOTE] Display initialization message to the user during startup.
echo [INFO] Starting the RVC WebUI program. Please wait up to 20 seconds...

:: [NOTE] Execute the main python script using the predefined absolute path for stability.
"B:\Thai RVC WebUI\runtime\python.exe" -I webui.py --pycmd "B:\Thai RVC WebUI\runtime\python.exe" --port 7897
pause