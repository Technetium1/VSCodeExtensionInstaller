#!/usr/bin/env bash
cd "$(dirname "$0")"
python3.9 -m pip install -U -r requirements.txt
pyinstaller -F --clean VSCodeExtensionInstaller.py
cp -f VSCodeExtensions.txt dist/VSCodeExtensions.txt
chmod +x dist/VSCodeExtensions
