:: ==========================================
:: File: Install_Environment.bat | Version: 1.0
:: Made and Checked By DELTA SYNTH And Gemini Claude and ChatGPT
:: Original By RVC Project
:: ==========================================
@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

:: Force execution in the current script directory
cd /d "%~dp0"

color 0A
echo ===============================================================
echo        DELTA SYNTH - RVC Environment Auto Installer
echo ===============================================================
echo.
echo [INFO] This script will install Global tools and Local dependencies.
echo.
pause

echo.
echo ===============================================================
echo [1/3] Installing Global Tools...
echo ===============================================================
winget install -e --id Python.Python.3.10 --accept-source-agreements --accept-package-agreements
winget install -e --id Git.Git --accept-source-agreements --accept-package-agreements
winget install -e --id Gyan.FFmpeg --accept-source-agreements --accept-package-agreements

echo.
echo ===============================================================
echo [2/3] Creating Local Virtual Environment...
echo ===============================================================
if not exist "venv" (
    echo [INFO] Creating virtual environment (venv)...
    "B:\Thai RVC WebUI\runtime\python.exe" -m venv venv
    echo [SUCCESS] Virtual environment created successfully!
) else (
    echo [SKIP] Virtual environment already exists.
)

echo.
echo ===============================================================
echo [3/3] Downloading and Installing RVC Dependencies...
echo ===============================================================
call venv\Scripts\activate.bat

"B:\Thai RVC WebUI\runtime\python.exe" -m pip install --upgrade pip

echo [INFO] Installing PyTorch and Torchvision...
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

if exist "requirements.txt" (
    echo [INFO] Installing dependencies from requirements.txt...
    pip install -r requirements.txt
) else (
    echo [WARNING] requirements.txt not found! The program may not function properly.
)

echo.
color 0E
echo ===============================================================
echo    Installation Completed Successfully!
echo ===============================================================
echo.
pause
exit