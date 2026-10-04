"""
Demo script - showcases the complete system capabilities
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from model import SkinCancerNet, count_parameters
from predict import predict_image, print_diagnosis, load_model
from data_loader import generate_synthetic_lesion, CLASSES
import torch
from PIL import Image

def demo_model_info():
    """Display model architecture information"""
    print("\n" + "=" * 70)
    print("  🧠 MODEL ARCHITECTURE DEMO")
    print("=" * 70)

    model = SkinCancerNet()
    total, trainable = count_parameters(model)

    print(f"\n  Model: SkinCancerNet")
    print(f"  Total Parameters: {total:,}")
    print(f"  Trainable Parameters: {trainable:,}")
    print(f"  Input Shape: (3, 224, 224) RGB")
    print(f"  Output Classes: {model.num_classes}")
    print(f"  Device: {torch.device('cuda' if torch.cuda.is_available() else 'cpu')}")

    print("\n  Classes Detected:")
    for i, info in model.CLASS_INFO.items():
        print(f"    {i}. {info['name']:35s} → {info['stage']:30s} ({info['severity']})")

    print("\n  Architecture Components:")
    print("    ✓ Residual Convolutional Blocks (4 layers)")
    print("    ✓ Channel Attention (Squeeze-and-Excitation)")
    print("    ✓ Multi-task Head (Classification + Malignancy Regression)")
    print("    ✓ Global Average Pooling")
    print("    ✓ Dropout Regularization (0.4)")


def demo_synthetic_generation():
    """Demonstrate synthetic lesion generation"""
    print("\n" + "=" * 70)
    print("  🎨 SYNTHETIC LESION GENERATION DEMO")
    print("=" * 70)

    demo_dir = "demo_synthetic_samples"
    os.makedirs(demo_dir, exist_ok=True)

    print(f"\n  Generating sample lesions for each class...\n")

    for class_id, info in CLASSES.items():
        img = generate_synthetic_lesion(class_id, size=(224, 224))
        filename = f"sample_class_{class_id}_{info['name'].replace(' ', '_')}.png"
        filepath = os.path.join(demo_dir, filename)
        img.save(filepath)
        print(f"    ✓ Created: {filename:50s} [{info['name']}]")

    print(f"\n  All samples saved to: {demo_dir}/")


def demo_predictions():
    """Run predictions on synthetic samples"""
    print("\n" + "=" * 70)
    print("  🔬 PREDICTION DEMO")
    print("=" * 70)

    try:
        model = load_model()
        print("\n  ✓ Model loaded successfully")
    except FileNotFoundError:
        print("\n  ⚠️  Trained model not found. Run 'python src/train_model.py' first.")
        return

    print("\n  Generating test lesions and running inference...\n")

    # Test 3 different classes
    test_classes = [0, 1, 3]  # Benign, Melanoma Early, BCC

    for class_id in test_classes:
        img = generate_synthetic_lesion(class_id, size=(224, 224))
        result = predict_image(img, model)

        print(f"  {'-' * 68}")
        print(f"  True Class: {CLASSES[class_id]['name']}")
        print(f"  Predicted:  {result['condition']} ({result['confidence']:.1f}% confidence)")
        print(f"  Stage:      {result['cancer_stage']}")
        print(f"  Risk:       {result['severity']}")
        print(f"  Malignancy: {result['malignancy_score']:.1f}%")

    print(f"  {'-' * 68}")


def demo_full_diagnosis():
    """Show a complete detailed diagnosis report"""
    print("\n" + "=" * 70)
    print("  📋 FULL DIAGNOSIS REPORT DEMO")
    print("=" * 70)

    try:
        model = load_model()
    except FileNotFoundError:
        print("\n  ⚠️  Trained model not found. Run 'python src/train_model.py' first.")
        return

    # Generate a melanoma sample
    img = generate_synthetic_lesion(class_id=1, size=(224, 224))
    result = predict_image(img, model)
    print_diagnosis(result)


def main():
    """Run all demos"""
    print("\n" + "█" * 70)
    print("  🔬 SKIN CANCER DETECTION SYSTEM - INTERACTIVE DEMO")
    print("█" * 70)

    demos = {
        '1': ("Model Architecture Info", demo_model_info),
        '2': ("Synthetic Lesion Generation", demo_synthetic_generation),
        '3': ("Quick Predictions", demo_predictions),
        '4': ("Full Diagnosis Report", demo_full_diagnosis),
        '5': ("Run All Demos", lambda: [demo_model_info(), demo_synthetic_generation(),
                                        demo_predictions(), demo_full_diagnosis()])
    }

    print("\n  Select Demo:")
    for key, (name, _) in demos.items():
        print(f"    {key}. {name}")
    print("    0. Exit")

    choice = input("\n  Enter choice (0-5): ").strip()

    if choice == '0':
        print("\n  Goodbye!")
        return

    if choice in demos:
        name, func = demos[choice]
        func()
    else:
        print("\n  Invalid choice!")

    print("\n" + "=" * 70)
    print("  Demo complete. Try running the web UI: python src/app.py")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
