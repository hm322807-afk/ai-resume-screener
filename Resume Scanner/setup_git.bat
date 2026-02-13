@echo off
echo Step 1: Checking Git installation...
git --version
if %errorlevel% neq 0 (
    echo [ERROR] Git is not installed or not in PATH.
    echo Please install Git from https://git-scm.com/download/win and run this script again.
    pause
    exit /b
)

echo.
echo Step 2: Initializing Repository...
git init
if %errorlevel% neq 0 (
    echo [ERROR] Failed to initialize repository.
    pause
    exit /b
)

echo.
echo Step 3: Configuring User (If needed)...
set /p name="Enter your GitHub Name (e.g., John Doe): "
set /p email="Enter your GitHub Email: "
git config user.name "%name%"
git config user.email "%email%"

echo.
echo Step 4: Adding Files...
git add .
git commit -m "Initial commit of AI Resume Screener V3"

echo.
echo [SUCCESS] Local repository created!
echo.
echo Step 5: Push to GitHub...
echo Go to https://github.com/new and create a new repository named 'ai-resume-screener'.
echo Then run the following commands manually:
echo.
echo git remote add origin https://github.com/YOUR_USERNAME/ai-resume-screener.git
echo git branch -M main
echo git push -u origin main
echo.
pause
