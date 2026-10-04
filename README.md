# Skin Cancer Detection & Staging ML System

A complete machine learning pipeline that:
- **Detects** skin cancer conditions from dermoscopic images
- **Classifies** them into 6 diagnostic categories
- **Determines staging** and severity risk for each diagnosis
- **Provides** an interactive web UI for predictions

## Cancer Types & Stages Detected

| Class | Condition | Type | Stage | Risk |
|-------|-----------|------|-------|------|
| 0 | Benign Nevus (Mole) | Benign | Stage 0 – Non-Cancerous | Low |
| 1 | Melanoma (Early) | Malignant | Stage I – Localized | High |
| 2 | Melanoma (Advanced) | Malignant | Stage II-III – Invasive | Critical |
| 3 | Basal Cell Carcinoma | Malignant | Stage I-II – Localized Basal | Moderate-High |
| 4 | Actinic Keratosis | Pre-malignant | Pre-cancerous / In-situ | Moderate |
| 5 | Benign Keratosis (BKL) | Benign | Stage 0 – Non-Cancerous | Low |

## Quick Start

```bash
cd skin_cancer_detection

# 1. Build dataset (downloads samples + generates synthetic training data)
python src/data_loader.py

# 2. Train the model
python src/train_model.py

# 3. Launch interactive web UI
python src/app.py
```

## Project Structure

```
skin_cancer_detection/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/              # Downloaded web samples
│   ├── processed/        # Training-ready images (6 classes)
│   ├── models/           # Saved trained models
│   └── dataset_metadata.csv
├── src/
│   ├── data_loader.py    # Dataset builder & synthetic generator
│   ├── model.py          # CNN architecture (SkinCancerNet)
│   ├── train_model.py    # Full training pipeline
│   ├── predict.py        # Single-image prediction engine
│   ├── evaluate.py       # Evaluation, metrics & visualizations
│   └── app.py            # Gradio web interface
├── results/              # Training plots & confusion matrices
└── tests/
    └── test_pipeline.py  # End-to-end tests
```

## ⚕️ Medical Disclaimer
This tool is for **educational and research purposes only**.
It is NOT a substitute for professional medical diagnosis.
Always consult a dermatologist for proper skin cancer screening.
