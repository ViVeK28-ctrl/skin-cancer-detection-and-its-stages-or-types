@echo off
REM Quick Start Script for Skin Cancer Detection System
echo ========================================
echo Skin Cancer Detection - Quick Start
echo ========================================
echo.

REM Check if virtual environment exists
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
    echo.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo.
echo Installing dependencies...
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu -q
pip install numpy pandas matplotlib seaborn scikit-learn pillow requests tqdm gradio -q

echo.
echo ========================================
echo Select an option:
echo ========================================
echo 1. Build Dataset (150 samples per class)
echo 2. Train Model (30 epochs)
echo 3. Test Model
echo 4. Launch Web UI
echo 5. Predict Single Image
echo 6. Evaluate Model
echo 7. Run Full Pipeline (Build + Train + Evaluate + Launch UI)
echo ========================================
echo.

set /p choice="Enter choice (1-7): "

if "%choice%"=="1" (
    echo Building dataset...
    python src\data_loader.py
    pause
) else if "%choice%"=="2" (
    echo Training model...
    python src\train_model.py
    pause
) else if "%choice%"=="3" (
    echo Running tests...
    python tests\test_pipeline.py
    pause
) else if "%choice%"=="4" (
    echo Launching web UI...
    python src\app.py
) else if "%choice%"=="5" (
    set /p img_path="Enter image path: "
    python src\predict.py %img_path%
    pause
) else if "%choice%"=="6" (
    echo Evaluating model...
    python src\evaluate.py
    pause
) else if "%choice%"=="7" (
    echo Running full pipeline...
    python src\data_loader.py
    python src\train_model.py
    python src\evaluate.py
    echo.
    echo Pipeline complete! Launching web UI...
    python src\app.py
) else (
    echo Invalid choice!
    pause
)
