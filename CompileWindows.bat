@echo off
TITLE PyInstaller
python -V > NUL 2> NUL
IF errorlevel 1 ECHO PYTHON NOT IN PATH! && PAUSE && EXIT
CD %~dp0
python -m pip install -U -r requirements.txt
pyinstaller -F -i vscode.ico --clean VSCodeExtensionInstaller.py
ECHO Copying VSCodeExtensions.txt
COPY .\VSCodeExtensions.txt .\dist\VSCodeExtensions.txt
RMDIR /S /Q build
DEL /q VSCodeExtensionInstaller.spec
ECHO Done! File is located in %~dp0dist
PAUSE
EXIT
