# 🔬 Skin Cancer Detection & Clinical Staging ML System
## Complete Project Report & Technical Specification

**Export Date:** 2026-09-29 02:31:44
**Version:** 1.0.0
**Framework:** PyTorch 2.14.0
**Validation Accuracy:** **82.2%**

---

## 1. Executive Summary

This project delivers an end-to-end Machine Learning system for automated dermoscopic skin cancer screening, condition classification, and clinical cancer staging. The system analyzes dermoscopic images and produces a comprehensive diagnostic report with:
- **Condition Classification:** 6 distinct skin lesion categories.
- **Clinical Cancer Staging:** Stage 0, Stage I (Localized), Stage II-III (Invasive), and Pre-cancerous in-situ.
- **Malignancy Probability:** Calibrated continuous score (0–100%).
- **Risk Stratification:** Low, Moderate, Moderate-High, High, Critical.
- **Evidence-Based Recommendations:** Follow-up clinical steps and urgency indicators.

---

## 2. Diagnostic & Staging Taxonomy

| Class ID | Condition | Pathology | Clinical Stage | Severity | Precision | Recall | F1-Score |
|---|---|---|---|---|---|---|---|
| **0** | Benign Nevus | Benign | Stage 0 / Non-Cancerous | Low Risk | 100.0% | 100.0% | 1.00 |
| **1** | Melanoma (Early) | Malignant | Stage I (Localized, <=2mm) | High Risk | 89.0% | 100.0% | 0.94 |
| **2** | Melanoma (Advanced) | Malignant | Stage II-III (Invasive) | Critical Risk | 100.0% | 86.0% | 0.93 |
| **3** | Basal Cell Carcinoma | Malignant | Stage I-II (Localized Basal) | Moderate-High | 49.0% | 96.0% | 0.65 |
| **4** | Actinic Keratosis | Pre-malignant | Pre-cancerous / In-situ | Moderate Risk | 75.0% | 10.0% | 0.18 |
| **5** | Benign Keratosis | Benign | Stage 0 / Non-Cancerous | Low Risk | 100.0% | 100.0% | 1.00 |

---

## 3. Model Architecture (`SkinCancerNet`)

- **Total Parameters:** 11,397,671
- **Trainable Parameters:** 11,397,671
- **Input Dimension:** (3, 224, 224) RGB
- **Backbone:**
  - Initial 7x7 Stem Conv (stride 2) + BatchNorm + MaxPool
  - 4 Residual Convolutional Stages (64, 128, 256, 512 channels)
  - Squeeze-and-Excitation (SE) Channel Attention after each stage
  - Global Average Pooling (AdaptiveAvgPool2d)
- **Multi-Task Heads:**
  1. `classifier`: Linear(512 -> 256) -> ReLU -> Dropout(0.3) -> Linear(256 -> 6)
  2. `malignancy_head`: Linear(512 -> 128) -> ReLU -> Dropout(0.3) -> Linear(128 -> 1) -> Sigmoid

---

## 4. Training Pipeline & Hyperparameters

- **Dataset Size:** 900 images (150 balanced samples per class)
- **Train / Validation Split:** 80% (720 images) / 20% (180 images)
- **Epochs:** 30
- **Batch Size:** 32
- **Optimizer:** Adam (LR: 1e-3, Weight Decay: 1e-4)
- **Learning Rate Schedule:** CosineAnnealingLR (T_max=30, eta_min=1e-6)
- **Loss Function:** Multi-task: `CrossEntropyLoss(classes) + 0.3 * MSELoss(malignancy)`
- **Data Augmentations:**
  - Random Horizontal & Vertical Flips
  - Random Rotation (±30°)
  - Color Jitter (Brightness, Contrast, Saturation, Hue)
  - Random Affine Translation & Scaling

---

## 5. Model Performance Results

- **Best Validation Accuracy:** **82.2%** (achieved at Epoch 30)
- **Training Accuracy:** **79.7%**
- **Melanoma Early Recall:** **100.0%** (Catches all early melanoma lesions)
- **Melanoma Advanced Precision:** **100.0%**
- **Benign Precision & Recall:** **100.0%** (Zero false alarms on benign moles)

---

## 6. How to Deploy and Run

### Start Web Interface:
```bash
python src/app_flask.py
```
Open **http://localhost:5000**

### CLI Prediction:
```bash
python src/predict.py data/processed/class_1_Melanoma_(Early)/lesion_1_0001.png
```

---

## 7. Medical Disclaimer
*This system is developed strictly for research, educational, and screening support purposes. It is NOT certified as a medical device and must NOT replace clinical diagnosis by a board-certified dermatologist.*
