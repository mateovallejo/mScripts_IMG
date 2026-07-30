@echo off
setlocal EnableExtensions EnableDelayedExpansion

set "PROJECT_DIR=%~dp0"
if "%PROJECT_DIR:~-1%"=="\" set "PROJECT_DIR=%PROJECT_DIR:~0,-1%"

echo Adding "%PROJECT_DIR%" to your user PATH...

set "USER_PATH="
for /f "skip=2 tokens=1,2,*" %%A in ('reg query "HKCU\Environment" /v PATH 2^>nul') do (
    if /I "%%A"=="PATH" set "USER_PATH=%%C"
)

echo !USER_PATH! | findstr /I /C:"%PROJECT_DIR%" >nul
if errorlevel 1 (
    if defined USER_PATH (
        set "NEW_PATH=!USER_PATH!;%PROJECT_DIR%"
    ) else (
        set "NEW_PATH=%PROJECT_DIR%"
    )

    setx PATH "!NEW_PATH!"
    echo Done.
) else (
    echo "%PROJECT_DIR%" is already in your user PATH.
)

echo.
echo Open a new terminal window for the change to take effect.
pause