@echo off
title AI Resume Screener - GitHub Deployment Wizard
color 0A

echo ========================================================
echo       AI RESUME SCREENER - DEPLOYMENT WIZARD
echo ========================================================
echo.

echo [1/5] Checking Git installation...
git --version
if %errorlevel% neq 0 (
    color 0C
    echo [ERROR] Git is NOT installed.
    echo Please install it from: https://git-scm.com/download/win
    pause
    exit /b
)
echo [OK] Git is ready.
echo.

echo [2/5] Configuring User Identity...
echo (This is needed for GitHub to know who wrote the code)
echo.
set /p name="> Enter your GitHub Name (e.g. John Doe): "
set /p email="> Enter your GitHub Email (e.g. john@email.com): "

git config --global user.name "%name%"
git config --global user.email "%email%"
echo [OK] User configured.
echo.

echo [3/5] preparing Repository...
if not exist ".git" (
    git init
    echo [OK] Repository initialized.
) else (
    echo [OK] Repository already exists.
)

git add .
git commit -m "Final Deployment of AI Resume Screener V3"
echo [OK] Code committed.
echo.

echo [4/5] Connecting to GitHub...
echo --------------------------------------------------------
echo ACTION REQUIRED:
echo 1. Go to https://github.com/new
echo 2. Name the repository: ai-resume-screener
echo 3. Click 'Create repository' at the bottom.
echo 4. Copy the HTTPS URL (looks like https://github.com/YourName/repo.git)
echo --------------------------------------------------------
echo.
set /p repo_url="> Paste the GitHub Repository URL here: "

git remote remove origin >nul 2>&1
git remote add origin %repo_url%
git branch -M main

echo.
echo [5/5] Pushing to GitHub...
echo (A browser window might pop up to ask for your GitHub password/login)
echo.
git push -u origin main

if %errorlevel% neq 0 (
    color 0C
    echo.
    echo [ERROR] Push failed. 
    echo Check your URL or Internet connection and try again.
) else (
    echo.
    echo ========================================================
    echo      SUCCESS! DEPLOYMENT COMPLETE! 🚀
    echo ========================================================
)
pause
