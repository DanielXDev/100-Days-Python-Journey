@echo off
setlocal enabledelayedexpansion

:: Define the repository name
set "REPO_NAME=100-Days-Python-Journey"

:: Create the repository folder
mkdir %REPO_NAME%
cd %REPO_NAME%

:: Create directories for days in batches of 10
for /L %%i in (1,10,91) do (
    set /A "start=%%i"
    set /A "end=%%i+9"
    
    :: Format numbers with leading zeros
    set "start=00!start!"
    set "end=00!end!"
    
    set "start=!start:~-3!"
    set "end=!end:~-3!"
    
    mkdir "Day-!start!...!end!"
)

:: Create essential files
echo # %REPO_NAME% > README.md
echo *.log > .gitignore
echo @echo off > create_dirs.sh
echo echo "This is a placeholder script for creating directories." >> create_dirs.sh

:: Initialize Git repository
git init
git add .
git commit -m "Initial commit with folder structure"

echo Repository structure created successfully!
