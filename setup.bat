@echo off
setlocal ENABLEDELAYEDEXPANSION


set package_name=_3d_rendering_engine
set files=__init__.py __main__.py matrix_calculations.py
set python_location=%localappdata%\Programs\Python\Python313
set target=nul


if not exist %python_location% (
	echo "%python_location%" not found!
	set /P python_location="Python39 directory location: "
	if not exist !python_location! (
		echo "!python_location!" not found!
		pause
		EXIT /B 0
	)
)

set target=%python_location%\Lib\site-packages

if not exist %target% (
	echo "%target%" not found, please make sure you have Python 3.9 installed correctly!
	pause
	EXIT /B 0
)

set target=%target%\%package_name%

if not exist %target% (
	echo Creating package directory!
	mkdir %target%
	if not exist %target% (
		echo Error while creating package directory!
		echo %target%
		pause
		EXIT /B 0
	)
)


(for %%a in (%files%) do (
	if exist %%a (
		if exist %target%\%%a (
			fc %%a %target%\%%a > nul
			if errorlevel 1 (
				echo %%a exists in target directory but contains different data:
				COPY "%%a" "%target%"
			)
		) else (
			echo %%a not found in target directory:
			COPY "%%a" "%target%"
		)
	) else (
		echo %%a not found in current directory! Please re-install installer.
	)
))


pause
EXIT /B 0


:YorN
set /P answer="%~1 (y/n)? "
if "%answer%" == "y" (
	set %~2=1
) else if "%answer%" == "n" (
	set %~2=0
) else (
	CALL :YorN "%~1" "%~2"
)
EXIT /B 0
