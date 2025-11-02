@echo off
title RAPIDRAG - External Access Mode

echo ========================================================================
echo                   RAPIDRAG - EXTERNAL ACCESS MODE
echo ========================================================================
echo.
echo                        WARNING: SECURITY RISK
echo ========================================================================
echo.
echo This mode exposes RAPIDRAG to the INTERNET.
echo.
echo RISKS:
echo   - Anyone with your public IP can access RAPIDRAG
echo   - No built-in authentication
echo   - Your documents are visible to anyone
echo   - Potential security vulnerabilities
echo.
echo REQUIREMENTS:
echo   - Port forwarding configured on router (port 8501)
echo   - Static IP or Dynamic DNS recommended
echo   - Firewall configured properly
echo.
echo ========================================================================
echo.
set /p confirm="Are you sure you want to enable external access? (Y/N): "

if /i not "%confirm%"=="Y" (
    echo.
    echo External access cancelled.
    pause
    exit /b
)

echo.
echo ========================================================================
echo STARTING RAPIDRAG WITH EXTERNAL ACCESS
echo ========================================================================
echo.

:: Get local IP
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr /c:"IPv4 Address"') do (
    set LOCALIP=%%a
    goto :found_local
)

:found_local
set LOCALIP=%LOCALIP: =%

echo Local IP Address: %LOCALIP%
echo.
echo ========================================================================
echo TO ACCESS EXTERNALLY:
echo ========================================================================
echo.
echo 1. Find your public IP: https://whatismyipaddress.com
echo 2. Share this URL: http://YOUR-PUBLIC-IP:8501
echo 3. Ensure port 8501 is forwarded to %LOCALIP%
echo.
echo ========================================================================
echo INTERNAL ACCESS:
echo ========================================================================
echo.
echo Local: http://localhost:8501
echo LAN:   http://%LOCALIP%:8501
echo.
echo ========================================================================
echo.
echo Press Ctrl+C to stop the server
echo.
echo ========================================================================
echo.

py -m streamlit run webapp.py --server.address 0.0.0.0 --server.port 8501

pause
