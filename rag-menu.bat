@echo off
setlocal enabledelayedexpansion
title RAG Chatbot - Control Panel

:: Set colors (if supported)
color 0A

:MAIN_MENU
cls
echo ========================================================================
echo                    RAG CHATBOT - CONTROL PANEL
echo ========================================================================
echo.
echo   Current Directory: %CD%
echo.
echo   [SETUP]
echo   1. First-Time Setup (Install dependencies + configure)
echo   2. Install/Update Python Dependencies
echo   3. Install Ollama + Download Model
echo   4. Run Setup Wizard (Configure .env)
echo.
echo   [OPERATIONS]
echo   5. Ingest Documents (Add to knowledge base)
echo   6. Start Chatbot (CLI - Interactive chat)
echo   7. Start Web Interface (Local Only)
echo   8. Start Web Interface (Network/LAN Access)
echo   9. Start Web Interface (External/Internet Access)
echo   10. Switch LLM Provider (OpenAI ^<-^> Ollama)
echo.
echo   [TESTING]
echo   11. Test System Setup
echo   12. Quick Q^&A Test
echo   13. Compare OpenAI vs Ollama
echo.
echo   [UTILITIES]
echo   14. View Documentation
echo   15. Open Documents Folder
echo   16. View System Status
echo.
echo   0. Exit
echo.
echo ========================================================================
set /p choice="Select option (0-16): "

if "%choice%"=="1" goto FIRST_TIME_SETUP
if "%choice%"=="2" goto INSTALL_DEPS
if "%choice%"=="3" goto INSTALL_OLLAMA
if "%choice%"=="4" goto RUN_SETUP
if "%choice%"=="5" goto INGEST_DOCS
if "%choice%"=="6" goto START_CHAT
if "%choice%"=="7" goto START_WEBAPP
if "%choice%"=="8" goto START_WEBAPP_NETWORK
if "%choice%"=="9" goto START_WEBAPP_EXTERNAL
if "%choice%"=="10" goto SWITCH_PROVIDER
if "%choice%"=="11" goto TEST_SETUP
if "%choice%"=="12" goto TEST_CHAT
if "%choice%"=="13" goto COMPARE_MODELS
if "%choice%"=="14" goto VIEW_DOCS
if "%choice%"=="15" goto OPEN_DOCS_FOLDER
if "%choice%"=="16" goto SYSTEM_STATUS
if "%choice%"=="0" goto EXIT

echo Invalid choice. Please try again.
timeout /t 2 >nul
goto MAIN_MENU

:FIRST_TIME_SETUP
cls
echo ========================================================================
echo                      FIRST-TIME SETUP
echo ========================================================================
echo.
echo This will:
echo   1. Install all Python dependencies
echo   2. Run the configuration wizard
echo   3. Create sample documents
echo.
echo This may take 5-10 minutes...
echo.
pause
echo.
echo [Step 1/3] Installing Python dependencies...
py -m pip install -r requirements.txt
if errorlevel 1 (
    echo.
    echo ERROR: Failed to install dependencies
    echo Please ensure Python is installed and in PATH
    pause
    goto MAIN_MENU
)
echo.
echo [Step 2/3] Running configuration wizard...
py setup.py
if errorlevel 1 (
    echo.
    echo ERROR: Configuration wizard failed
    pause
    goto MAIN_MENU
)
echo.
echo [Step 3/3] Loading sample documents...
py ingest_documents.py --samples
echo.
echo ========================================================================
echo SETUP COMPLETE!
echo ========================================================================
echo.
echo Next steps:
echo   - If using Ollama, install it from: https://ollama.ai
echo   - Run option 3 to download Ollama model
echo   - Or configure OpenAI API key in .env
echo.
echo You can now use option 6 to start chatting!
echo.
pause
goto MAIN_MENU

:INSTALL_DEPS
cls
echo ========================================================================
echo                  INSTALLING PYTHON DEPENDENCIES
echo ========================================================================
echo.
echo Installing all required packages...
echo.
py -m pip install -r requirements.txt
if errorlevel 1 (
    echo.
    echo ERROR: Installation failed
    pause
    goto MAIN_MENU
)
echo.
echo ========================================================================
echo Dependencies installed successfully!
echo ========================================================================
echo.
pause
goto MAIN_MENU

:INSTALL_OLLAMA
cls
echo ========================================================================
echo                  OLLAMA INSTALLATION HELPER
echo ========================================================================
echo.
echo Checking if Ollama is installed...
echo.

:: Check if Ollama is in PATH
where ollama >nul 2>&1
if %errorlevel%==0 (
    echo Ollama is already installed!
    echo.
    ollama --version
    echo.
) else (
    :: Check common installation path
    if exist "C:\Users\%USERNAME%\AppData\Local\Programs\Ollama\ollama.exe" (
        echo Ollama is installed but not in PATH.
        set "OLLAMA_CMD=C:\Users\%USERNAME%\AppData\Local\Programs\Ollama\ollama.exe"
    ) else (
        echo Ollama is NOT installed.
        echo.
        echo Please download and install Ollama from:
        echo https://ollama.ai/download/windows
        echo.
        echo After installation, run this option again to download the model.
        pause
        goto MAIN_MENU
    )
)

echo.
echo ========================================================================
echo Would you like to download the llama3.2 model?
echo (This will download ~2GB and may take several minutes)
echo ========================================================================
echo.
set /p download="Download model now? (Y/N): "
if /i not "%download%"=="Y" goto MAIN_MENU

echo.
echo Downloading llama3.2 model...
echo This may take 5-10 minutes depending on your connection...
echo.

if defined OLLAMA_CMD (
    "%OLLAMA_CMD%" pull llama3.2
) else (
    ollama pull llama3.2
)

if errorlevel 1 (
    echo.
    echo ERROR: Model download failed
    pause
    goto MAIN_MENU
)

echo.
echo ========================================================================
echo Model downloaded successfully!
echo ========================================================================
echo.
echo You can now use Ollama with the chatbot.
echo Make sure .env has: LLM_PROVIDER=ollama
echo.
pause
goto MAIN_MENU

:RUN_SETUP
cls
echo ========================================================================
echo                    CONFIGURATION WIZARD
echo ========================================================================
echo.
py setup.py
echo.
pause
goto MAIN_MENU

:INGEST_DOCS
cls
echo ========================================================================
echo                    DOCUMENT INGESTION
echo ========================================================================
echo.
echo Choose ingestion type:
echo.
echo   1. Ingest from documents/ folder (your files)
echo   2. Load sample documents (for testing)
echo   3. Specify custom folder
echo   0. Back to main menu
echo.
set /p ingest_choice="Select option (0-3): "

if "%ingest_choice%"=="1" goto INGEST_LOCAL
if "%ingest_choice%"=="2" goto INGEST_SAMPLES
if "%ingest_choice%"=="3" goto INGEST_CUSTOM
if "%ingest_choice%"=="0" goto MAIN_MENU
goto INGEST_DOCS

:INGEST_LOCAL
echo.
echo Ingesting documents from documents/ folder...
echo.
py ingest_documents.py
echo.
pause
goto MAIN_MENU

:INGEST_SAMPLES
echo.
echo Loading sample documents...
echo.
py ingest_documents.py --samples
echo.
pause
goto MAIN_MENU

:INGEST_CUSTOM
echo.
set /p custom_path="Enter path to documents folder: "
echo.
echo Ingesting documents from %custom_path%...
echo.
py ingest_documents.py --source "%custom_path%"
echo.
pause
goto MAIN_MENU

:START_CHAT
cls
echo ========================================================================
echo                    STARTING CHATBOT (CLI)
echo ========================================================================
echo.
echo Loading RAG Chatbot...
echo.
echo Commands available in chatbot:
echo   - Type your question and press Enter
echo   - help    - Show available commands
echo   - info    - System information
echo   - history - Conversation history
echo   - exit    - Quit chatbot
echo.
echo ========================================================================
echo.
py chatbot.py
echo.
echo Chatbot closed.
pause
goto MAIN_MENU

:START_WEBAPP
cls
echo ========================================================================
echo                    STARTING WEB INTERFACE (LOCAL ONLY)
echo ========================================================================
echo.
echo Launching RAPIDRAG web dashboard...
echo.
echo Access: Local computer only
echo URL: http://localhost:8501
echo.
echo Features:
echo   - Lightning fast interface
echo   - Interactive chat
echo   - Document upload
echo   - Analytics dashboard
echo.
echo The browser will open automatically.
echo Press Ctrl+C in this window to stop the server.
echo.
echo ========================================================================
echo.
py -m streamlit run webapp.py
echo.
pause
goto MAIN_MENU

:START_WEBAPP_NETWORK
cls
echo ========================================================================
echo                    STARTING WEB INTERFACE (NETWORK ACCESS)
echo ========================================================================
echo.
echo Launching RAPIDRAG with network access enabled...
echo.
echo This allows anyone on your local network to access RAPIDRAG.
echo.
echo ========================================================================
echo.
call start-webapp-network.bat
echo.
pause
goto MAIN_MENU

:START_WEBAPP_EXTERNAL
cls
echo ========================================================================
echo                    STARTING WEB INTERFACE (EXTERNAL ACCESS)
echo ========================================================================
echo.
echo WARNING: This exposes RAPIDRAG to the INTERNET!
echo.
echo Only use if:
echo   - You have port forwarding configured
echo   - You understand the security risks
echo   - You trust who will access it
echo.
echo ========================================================================
echo.
call start-webapp-external.bat
echo.
pause
goto MAIN_MENU

:SWITCH_PROVIDER
cls
echo ========================================================================
echo                    SWITCH LLM PROVIDER
echo ========================================================================
echo.
py switch_provider.py
echo.
pause
goto MAIN_MENU

:TEST_SETUP
cls
echo ========================================================================
echo                    SYSTEM SETUP TEST
echo ========================================================================
echo.
echo Running system verification tests...
echo.
py tests/test_setup.py
echo.
pause
goto MAIN_MENU

:TEST_CHAT
cls
echo ========================================================================
echo                    QUICK Q&A TEST
echo ========================================================================
echo.
echo Running automated Q&A test...
echo.
py tests/test_chat.py
echo.
pause
goto MAIN_MENU

:COMPARE_MODELS
cls
echo ========================================================================
echo                  OPENAI VS OLLAMA COMPARISON
echo ========================================================================
echo.
echo Testing both providers (requires both configured)...
echo.
py tests/compare_models.py
echo.
pause
goto MAIN_MENU

:VIEW_DOCS
cls
echo ========================================================================
echo                      DOCUMENTATION
echo ========================================================================
echo.
echo Available documentation:
echo.
echo   1. Quick Start Guide (GET_STARTED.txt)
echo   2. File Formats Guide
echo   3. Privacy Guide
echo   4. Project Structure
echo   5. Full README
echo   6. Open docs folder in Explorer
echo   0. Back to main menu
echo.
set /p doc_choice="Select document (0-6): "

if "%doc_choice%"=="1" type docs\GET_STARTED.txt & pause & goto VIEW_DOCS
if "%doc_choice%"=="2" start "" docs\guides\FILE_FORMATS.md & goto VIEW_DOCS
if "%doc_choice%"=="3" start "" docs\guides\PRIVACY.md & goto VIEW_DOCS
if "%doc_choice%"=="4" start "" docs\STRUCTURE.md & goto VIEW_DOCS
if "%doc_choice%"=="5" start "" docs\README.md & goto VIEW_DOCS
if "%doc_choice%"=="6" explorer docs & goto VIEW_DOCS
if "%doc_choice%"=="0" goto MAIN_MENU
goto VIEW_DOCS

:OPEN_DOCS_FOLDER
explorer documents
goto MAIN_MENU

:SYSTEM_STATUS
cls
echo ========================================================================
echo                      SYSTEM STATUS
echo ========================================================================
echo.
echo Python Version:
py --version
echo.
echo -----------------------------------------------------------------------
echo.
echo Ollama Status:
where ollama >nul 2>&1
if %errorlevel%==0 (
    ollama --version
    echo Ollama: INSTALLED
) else (
    if exist "C:\Users\%USERNAME%\AppData\Local\Programs\Ollama\ollama.exe" (
        "C:\Users\%USERNAME%\AppData\Local\Programs\Ollama\ollama.exe" --version
        echo Ollama: INSTALLED (not in PATH)
    ) else (
        echo Ollama: NOT INSTALLED
    )
)
echo.
echo -----------------------------------------------------------------------
echo.
echo Configuration (.env):
if exist ".env" (
    echo .env file: EXISTS
    findstr "LLM_PROVIDER" .env
) else (
    echo .env file: NOT FOUND - Run setup wizard
)
echo.
echo -----------------------------------------------------------------------
echo.
echo Knowledge Base:
if exist "data\document_store.json" (
    echo Document store: EXISTS
    for %%A in ("data\document_store.json") do echo Size: %%~zA bytes
) else (
    echo Document store: NOT FOUND - Run document ingestion
)
echo.
echo -----------------------------------------------------------------------
echo.
echo Documents Folder:
if exist "documents" (
    dir /b documents | find /c /v "" > temp_count.txt
    set /p file_count=<temp_count.txt
    del temp_count.txt
    echo Documents: !file_count! files in documents/
) else (
    echo Documents folder: NOT FOUND
)
echo.
echo ========================================================================
echo.
pause
goto MAIN_MENU

:EXIT
cls
echo.
echo Thank you for using RAG Chatbot!
echo.
timeout /t 2 >nul
exit /b 0
