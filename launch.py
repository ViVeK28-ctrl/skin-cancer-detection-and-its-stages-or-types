"""
One-command launcher - starts the complete skin cancer detection system
"""

import os
import sys
import subprocess

def check_model_exists():
    """Check if trained model exists"""
    model_path = os.path.join("data", "models", "skin_cancer_best.pth")
    return os.path.exists(model_path)

def check_dataset_exists():
    """Check if dataset has been built"""
    dataset_path = os.path.join("data", "dataset_metadata.csv")
    return os.path.exists(dataset_path)

def print_header():
    print("\n" + "=" * 70)
    print("  🔬 SKIN CANCER DETECTION & STAGING SYSTEM")
    print("=" * 70 + "\n")

def main():
    print_header()

    # Check prerequisites
    if not check_dataset_exists():
        print("📦 Dataset not found. Building dataset...")
        subprocess.run([sys.executable, "src/data_loader.py"], check=True)
        print("✓ Dataset built successfully\n")

    if not check_model_exists():
        print("🧠 Trained model not found. Training model (this may take 20-30 minutes)...")
        print("    You can monitor progress in real-time.\n")
        subprocess.run([sys.executable, "src/train_model.py"], check=True)
        print("\n✓ Model trained successfully\n")
    else:
        print("✓ Found trained model")
        print("✓ Found dataset\n")

    # Launch web UI
    print("🚀 Launching web interface...")
    print("   Opening at: http://localhost:7860")
    print("   Press Ctrl+C to stop\n")
    print("-" * 70)

    try:
        subprocess.run([sys.executable, "src/app.py"], check=True)
    except KeyboardInterrupt:
        print("\n\n" + "=" * 70)
        print("  System stopped. Goodbye!")
        print("=" * 70 + "\n")
    except Exception as e:
        print(f"\n⚠️  Error: {e}")
        print("\nTroubleshooting:")
        print("  1. Install Gradio: pip install gradio")
        print("  2. Run console mode: python src/predict.py <image_path>")
        print("  3. Check logs in results/")

if __name__ == "__main__":
    main()
