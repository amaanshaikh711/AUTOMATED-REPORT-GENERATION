#!/bin/bash

# Insightify - GUI Application Launcher
# This script launches the Insightify GUI application

echo ""
echo "========================================"
echo "  INSIGHTIFY - Report Generator"
echo "  Professional Data Analysis System"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

# Check Python version
python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "Python version: $python_version"

# Check if required modules are installed
python3 -c "import PyQt6" 2>/dev/null
if [ $? -ne 0 ]; then
    echo ""
    echo "Installing required dependencies..."
    echo ""
    pip3 install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to install dependencies"
        exit 1
    fi
fi

# Launch the GUI application
echo ""
echo "Launching Insightify GUI Application..."
echo ""
python3 ui_application.py

if [ $? -ne 0 ]; then
    echo ""
    echo "ERROR: Failed to launch application"
    exit 1
fi
