#!/bin/bash
# Quick Start Script for Skin Cancer Detection System (Linux/Mac)

set -e

echo "========================================"
echo "Skin Cancer Detection - Quick Start"
echo "========================================"
echo

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo
echo "Installing dependencies..."
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu -q
pip install numpy pandas matplotlib seaborn scikit-learn pillow requests tqdm gradio -q

echo
echo "========================================"
echo "Select an option:"
echo "========================================"
echo "1. Build Dataset (150 samples per class)"
echo "2. Train Model (30 epochs)"
echo "3. Test Model"
echo "4. Launch Web UI"
echo "5. Predict Single Image"
echo "6. Evaluate Model"
echo "7. Run Full Pipeline (Build + Train + Evaluate + Launch UI)"
echo "========================================"
echo

read -p "Enter choice (1-7): " choice

case $choice in
    1)
        echo "Building dataset..."
        python src/data_loader.py
        ;;
    2)
        echo "Training model..."
        python src/train_model.py
        ;;
    3)
        echo "Running tests..."
        python tests/test_pipeline.py
        ;;
    4)
        echo "Launching web UI..."
        python src/app.py
        ;;
    5)
        read -p "Enter image path: " img_path
        python src/predict.py "$img_path"
        ;;
    6)
        echo "Evaluating model..."
        python src/evaluate.py
        ;;
    7)
        echo "Running full pipeline..."
        python src/data_loader.py
        python src/train_model.py
        python src/evaluate.py
        echo
        echo "Pipeline complete! Launching web UI..."
        python src/app.py
        ;;
    *)
        echo "Invalid choice!"
        exit 1
        ;;
esac
