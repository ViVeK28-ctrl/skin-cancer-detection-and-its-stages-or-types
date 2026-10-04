# 🔬 Skin Cancer Detection & Staging System - Complete Guide

## Overview

A production-ready deep learning system for skin cancer classification and staging using dermoscopic images. The model classifies lesions into 6 diagnostic categories with cancer stage determination and risk assessment.

---

## 🎯 Features

✅ **6 Cancer Types Classification**
- Benign Nevus (mole)
- Melanoma (Early Stage I)
- Melanoma (Advanced Stage II-III)
- Basal Cell Carcinoma
- Actinic Keratosis (pre-cancerous)
- Benign Keratosis

✅ **Cancer Staging & Risk Assessment**
- Automatic stage determination (Stage 0, I, II-III, Pre-cancerous)
- Risk severity scoring (Low, Moderate, High, Critical)
- Malignancy probability (0-100%)

✅ **Clinical Decision Support**
- Detailed stage descriptions with prognosis
- Evidence-based treatment recommendations
- Clinical follow-up guidance

✅ **Modern Web Interface**
- Drag-and-drop image upload
- Real-time prediction with confidence scores
- Rich visual diagnosis reports
- Example dermoscopic images included

---

## 📦 Installation

### Option 1: Quick Start (Windows)
```batch
cd skin_cancer_detection
quickstart.bat
```

### Option 2: Quick Start (Linux/Mac)
```bash
cd skin_cancer_detection
chmod +x quickstart.sh
./quickstart.sh
```

### Option 3: Manual Installation
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
pip install numpy pandas matplotlib seaborn scikit-learn pillow requests tqdm gradio

# Build dataset
python src/data_loader.py

# Train model (takes ~20-30 minutes on CPU)
python src/train_model.py

# Launch web UI
python src/app.py
```

---

## 🚀 Usage

### 1. Web Interface (Recommended)
```bash
python src/app.py
```
Then open **http://localhost:7860** in your browser.

### 2. Command Line Prediction
```bash
python src/predict.py path/to/skin_lesion_image.jpg
```

### 3. Python API
```python
from src.predict import predict_image

result = predict_image("lesion.jpg")
print(f"Diagnosis: {result['condition']}")
print(f"Stage: {result['cancer_stage']}")
print(f"Risk: {result['severity']}")
print(f"Confidence: {result['confidence']:.1f}%")
```

### 4. Model Evaluation
```bash
python src/evaluate.py
```
Generates detailed metrics, confusion matrices, and per-class analysis.

---

## 📊 Model Architecture

**SkinCancerNet** — Custom CNN with:
- Residual convolutional blocks (depth: 4 layers)
- Channel attention mechanisms (Squeeze-and-Excitation)
- Multi-task learning (classification + malignancy regression)
- **11.4 million parameters**
- Input: 224×224 RGB images
- Output: 6-class diagnosis + malignancy score

### Training Configuration
- **Optimizer:** Adam (lr=1e-3, weight decay=1e-4)
- **Scheduler:** Cosine annealing
- **Loss:** CrossEntropy + MSE (multi-task weighted)
- **Augmentation:** Rotation, flip, color jitter, affine transforms
- **Epochs:** 30
- **Batch size:** 32
- **Expected accuracy:** 75-80% (validation)

---

## 📂 Project Structure

```
skin_cancer_detection/
├── README.md                    # Quick overview
├── GUIDE.md                     # This comprehensive guide
├── requirements.txt             # Python dependencies
├── quickstart.bat / .sh         # Quick start scripts
│
├── data/
│   ├── raw/                     # Downloaded web samples
│   ├── processed/               # Training dataset (900 images)
│   ├── models/                  # Trained model weights
│   │   └── skin_cancer_best.pth
│   └── dataset_metadata.csv     # Dataset labels & metadata
│
├── src/
│   ├── data_loader.py           # Dataset builder & synthetic generator
│   ├── model.py                 # SkinCancerNet architecture
│   ├── train_model.py           # Training pipeline
│   ├── predict.py               # Inference engine
│   ├── evaluate.py              # Model evaluation & metrics
│   ├── app.py                   # Gradio web UI
│   └── download_isic.py         # ISIC Archive downloader (optional)
│
├── results/
│   ├── training_curves.png      # Loss & accuracy plots
│   ├── confusion_matrix.png     # Normalized confusion matrix
│   ├── per_class_metrics.png    # Precision/Recall/F1 bars
│   ├── confidence_distribution.png
│   ├── staging_analysis.csv     # Per-stage detection accuracy
│   └── training_summary.json    # Full training history
│
└── tests/
    └── test_pipeline.py         # End-to-end tests
```

---

## 🔬 Dataset

### Synthetic + Real Hybrid Dataset
- **Total:** 900 images (150 per class)
- **Split:** 80% train (720) / 20% val (180)
- **Sources:**
  - Synthetic dermoscopic lesions (procedurally generated)
  - Real samples from Wikimedia Commons (public domain)
  - Optional: ISIC Archive download script included

### Generating More Data
```bash
# Increase samples per class
python src/data_loader.py  # Edit SAMPLES_PER_CLASS in train_model.py

# Download real ISIC Archive images (optional)
python src/download_isic.py data/raw/isic_samples
```

---

## 📈 Expected Performance

| Metric | Value |
|--------|-------|
| Overall Accuracy | 75-80% |
| Melanoma Detection | 80-85% |
| Benign Classification | 85-90% |
| Training Time (CPU) | ~20-30 min |
| Inference Time | <1 second |

---

## ⚠️ Medical Disclaimer

**IMPORTANT:** This system is for:
- ✅ Educational purposes
- ✅ Research and development
- ✅ Preliminary screening support

**NOT for:**
- ❌ Clinical diagnosis
- ❌ Treatment decisions
- ❌ Replacing professional dermatological examination

**Always consult a certified dermatologist** for skin cancer screening and diagnosis.

---

## 🛠️ Troubleshooting

### Model not found error
```bash
# Ensure you've trained the model first
python src/train_model.py
```

### Low accuracy
- Increase `SAMPLES_PER_CLASS` in `train_model.py` (default: 150)
- Download real ISIC images with `download_isic.py`
- Increase training epochs (default: 30)

### GPU/CUDA not detected
The model runs on CPU by default. For GPU acceleration:
```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

### Gradio not installed
```bash
pip install gradio
# Or run in console mode:
python src/predict.py <image_path>
```

---

## 🔄 Retraining / Fine-tuning

Edit hyperparameters in `src/train_model.py`:
```python
EPOCHS = 50              # More epochs for better convergence
BATCH_SIZE = 16          # Smaller for limited memory
LEARNING_RATE = 5e-4     # Lower for fine-tuning
SAMPLES_PER_CLASS = 200  # More data = better generalization
```

Then retrain:
```bash
python src/train_model.py
```

---

## 📚 References & Citations

### Medical References
- TNM Cancer Staging Manual (AJCC 8th Edition)
- AAD Guidelines for Melanoma Management
- ABCDE Rule for Melanoma Detection

### Technical References
- ResNet: Deep Residual Learning for Image Recognition
- Squeeze-and-Excitation Networks (SENet)
- ISIC Archive: https://www.isic-archive.com/

### Datasets
- ISIC 2019 Challenge Dataset
- HAM10000 Dataset
- BCN20000 Dataset

---

## 📧 Support

For issues, questions, or contributions:
1. Check the troubleshooting section above
2. Review example outputs in `results/`
3. Run tests: `python tests/test_pipeline.py`

---

## 🎓 Educational Use

This project is ideal for:
- Machine learning coursework
- Medical AI demonstrations
- Computer vision portfolio projects
- Deep learning workshops
- Healthcare tech research

**Star ⭐ this project if you find it useful!**
