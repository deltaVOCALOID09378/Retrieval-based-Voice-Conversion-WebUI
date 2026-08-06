@echo off
title RVC WebUI Modular Launcher
color 0A

:: Force starting in the exact directory of this batch file
cd /d "%~dp0"

echo ==============================================================
echo [Initializing Modular WebUI]
echo Made and Checked By DELTA SYNTH And Gemini Claude and ChatGPT
echo Original By Patiphat Wongyai (Delta) ^& RVC Project
echo ==============================================================
echo.

:: Launch the infer-web.py script with the defined Python path and pass any dragged arguments
"B:\Thai RVC WebUI\runtime\python.exe" infer-web.py %*

echo.
echo ==============================================================
echo [Process Terminated or Completed]
echo ==============================================================
pause