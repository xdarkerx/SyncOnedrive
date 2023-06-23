@echo off

powershell -Command "Remove-Item -Recurse -Force -Path build -ErrorAction Continue"
powershell -Command "Remove-Item -Recurse -Force -Path dist -ErrorAction Continue"
powershell -Command "Remove-Item -Force -Path main.spec -ErrorAction Continue"
powershell -Command "pip install PyInstaller"
powershell -Command "python -m PyInstaller Fonte/main.py"

powershell -Command "$WshShell = New-Object -ComObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%~dp0\syncOneD.lnk'); $Shortcut.TargetPath = '%~dp0\dist\main\main.exe'; $Shortcut.Save()"

timeout /t 1 /nobreak >nul