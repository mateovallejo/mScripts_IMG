@echo off
if "%~1"=="" (
    echo Usage: PSDtoEXR.bat input.psd
    exit /b 1
)

set "input=%~1"
set "output=%~dpn1.exr"

python "%~dp0PSDtoEXR.py" "%input%" "%output%"
if errorlevel 1 (
    echo Error converting file
    exit /b 1
)
