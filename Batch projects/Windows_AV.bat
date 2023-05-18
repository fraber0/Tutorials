@echo off
title WindowsXPAV2.0
color 0e
echo welcome to WindowsXPAV2.0
echo NOTE: This program is still under development. type 'info' for informations
pause
pause
pause
echo.
echo -------------------------
echo      WindowsXPAV2.0
echo.
echo -------------------------
:Menu
echo What would you like to do?
echo.
set /p where=
echo.
if %where% == scan goto :scan
if %where% == info goto :info
if %where% == commands goto :commands
if %where% == changesettings goto :changesettings
if %where% == exit goto :exit
if not %where% == scan goto :error
if not %where% == info goto :error
if not %where% == commands goto :error
if not %where% == changesettings goto :error
if not %where% == exit goto :error
cd C:\Windows\system32

:scan
echo Scanning...
echo Scanning...
echo Scanning...
if exist [...] goto infected1
if exist [...] goto infected2
if exist [...] goto infected3
rem malwares...(any file or site)
if not exist [...] goto clean
if not exist [...] goto clean
if not exist [...] goto clean
rem malwares...(any file or site)

:infected1
echo [...] has been detected
echo Deleting [...]
del [...]
pause
goto :clean2

rem :infected2...3...

:clean
echo Scanned complete, no malware has been detected
pause
goto :Menu

:clean2
echo Malware has been deleted
echo Thank you for using WindowsXPAV2.0
pause
goto :Menu

:info
echo WindowsXPAV2.0 is a batch programmed tool that eliminates a specific target in a system directory
echo for commands type 'commands' in the text space..
pause
goto :Menu

:commands
echo SCAN: scan the system library.
echo INFO: get information about WindowsXPAV2.0.
echo COMMANDS: get all WindowsXPAV2.0 commands.
echo CHANGESETTINGS: change the settings.
echo EXIT: leave the program.
pause
goto :Menu

:changesettings
echo Settings is disabled due a coding error
goto :Menu

:error
echo This command is not available
pause
goto :Menu

:exit
echo Exiting the program
pause
exit
