@echo off

title Main Terminal
color 0f
echo By Parreglias_playground
echo NOTE: this program is under development, for any doubt type 'info'
pause
pause

echo  =================
echo      MAIN MENU  
echo  =================
echo.
:Menu
echo Welcome to the Main Terminal, what would you like to do?
echo.
set /p where=
echo.
if %where% == info goto :info
if %where% == commands goto :commands
if %where% == start goto :start
if %where% == USB goto :usb
if %where% == CMD goto cmd
if %where% == exit goto :exit
if not %where% == info goto :error
if not %where% == commands goto :error
if not %where% == start goto :error
if not %where% == USB goto :error
if not %where% == CMD goto :error
if not %where% == exit goto :error
cd C:\Windows\system32

:Menu1
echo What would you like to do next?
echo.
set /p where=
echo.
if %where% == info goto :info
if %where% == commands goto :commands
if %where% == start goto :start
if %where% == USB goto :start
if %where% == CMD goto cmd
if %where% == exit goto :exit
if not %where% == info goto :error
if not %where% == commands goto :error
if not %where% == start goto :error
if not %where% == USB goto :error
if not %where% == CMD goto :error
if not %where% == exit goto :error

:info
echo NOTE: this is a version adapted for Windows XP and versions before Windows 10
echo for programs adapted to windows 10 and 11 consult the website at this link:
echo ...
echo Main Terminal is a program developed for help people using Windows XP
echo for reading all the functions type 'commands' in the text space
pause
echo Closing...
pause
goto :Menu1

:commands
echo This is the list of all the functions of this program:
echo     INFO: Read all the infos about PDF_Editor Terminal.
echo COMMANDS: Read all the functions of this program.
echo    START: Run a PDF_Editor program.
echo      USB: Search for a USB path in the system.
echo      CMD: Open the CMD terrminal.
echo     EXIT: Leave the program.
pause
echo Closing...
pause
goto :Menu1

:start
echo This is the list of all the programs you can run:
echo.
echo 1Google
echo 2Notepad
echo 3WindowsXPAV2.0
echo.
echo If you want to leave this function type 'exit' in the text space
echo.
echo Welcome to the Start Menu, what would you like to do?
echo.
set /p where=
echo.
if %where% == Google goto :google
if %where% == Notepad goto :notepad
if %where% == WindowsXPAV2.0 goto :WindowsXPAV2.0
if %where% == exit goto :Menu
if not %where% == Google goto :error1
if not %where% == Notepad goto :error1
if not %where% == WindowsXPAV2.0 goto :error1
if not %where% == exit goto :error1

:usb
echo Searching for an USB path...
pause
if exist [...] goto usb1
if exist [...] goto usb2
if exist [...] goto usb3
if not exist [...] goto clean
if not exist [...] goto clean
if not exist [...] goto clean
pause
echo Closing...
pause
goto :Menu1

:cmd
echo Starting CMD terminal....
pause
start CMD
pause
echo Closing...
pause
goto :Menu1

:clean
echo No USB path has been found...
pause
echo Closing...
pause
goto :Menu1

:usb1
echo The USB path [...] has been found...
echo Do you want to open it?
echo.
set /p where=
echo.
if %where% == yes start [...]
if %where% == no goto :close
if not %where% == yes goto :error
if not %where% == no goto :error
goto :usb

:usb2
echo The USB path [...] has been found...
echo Do you want to open it?
echo.
set /p where=
echo.
if %where% == yes start [...]
if %where% == no goto :close
if not %where% == yes goto :error
if not %where% == no goto :error
pause
goto :usb

:usb3
echo The USB path [...] has been found...
echo Do you want to open it?
echo.
set /p where=
echo.
if %where% == yes start [...]
if %where% == no goto :close
if not %where% == yes goto :error
if not %where% == no goto :error
goto :usb

:close
echo Closing the function...
pause
goto :Menu1

:google
echo Starting Google...
pause
start www.google.com
pause
echo Closing...
pause
goto :start

:notepad
echo Starting Notepad...
pause
start Notepad
pause
echo Closing...
pause
goto :start

:WindowsXPAV2.0
echo Starting WindowsXPAV2.0...
pause
start WindowsXPAV2.0.bat
pause
echo Closing...
pause
goto :start


:error
echo The command typed is not available
pause
goto :Menu1

:error1
echo The program that you want to start is not available
pause
goto :start

:exit
echo Exiting...
pause
echo thank you for using PDF_Editor
pause
exit
