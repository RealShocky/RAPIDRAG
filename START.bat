@echo off
:: Quick launcher for RAG Chatbot
title RAG Chatbot - Quick Start

:: Check if first run
if not exist ".env" (
    echo ========================================================================
    echo                      FIRST-TIME SETUP REQUIRED
    echo ========================================================================
    echo.
    echo This appears to be your first time running the RAG Chatbot.
    echo.
    echo Would you like to run the automatic setup? This will:
    echo   - Install all Python dependencies
    echo   - Configure your system
    echo   - Load sample documents
    echo.
    set /p setup="Run automatic setup now? (Y/N): "
    if /i "!setup!"=="Y" (
        echo.
        echo Running first-time setup...
        call rag-menu.bat
        exit /b
    )
)

:: Launch main menu
call rag-menu.bat
