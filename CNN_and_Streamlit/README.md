# Intel Image Classification — CNN Mini-Project

**Name:** Aditya Roshan S (Aadi)
**Student ID:** 24BAI10227
**Program:** B.Tech AI/ML Engineering, VIT Bhopal University

## Overview

This mini-project trains a Convolutional Neural Network (CNN) on the **Intel Image
Classification** dataset to classify natural scene images into 6 categories, and deploys
the trained model through a simple **Streamlit** web app.

Classes: `buildings`, `forest`, `glacier`, `mountain`, `sea`, `street`

## Files in this submission

| File | Description |
|---|---|
| `1A_CNN_Intel_Image_Classification.ipynb` | CNN model — data loading, architecture, training logs, accuracy/loss plots, evaluation |
| `1B_streamlit_app.py` | Streamlit deployment app — image upload + prediction UI |
| `Mini_Project_Report.docx` | Project report |
| `README.md` | This file |

## Dataset

Download the **Intel Image Classification** dataset from Kaggle:
https://www.kaggle.com/datasets/puneet6060/intel-image-classification

Extract it into a `data/` folder next to the notebook so it looks like this:

```
data/
├── seg_train/
│   └── seg_train/
│       ├── buildings/
│       ├── forest/
│       ├── glacier/
│       ├── mountain/
│       ├── sea/
│       └── street/
└── seg_test/
    └── seg_test/
        ├── buildings/
        ├── forest/
        ├── glacier/
        ├── mountain/
        ├── sea/
        └── street/
```

## Setup

```bash
pip install tensorflow streamlit pillow numpy matplotlib scikit-learn seaborn
```

## How to run

### 1. Train the CNN

Open and run `1A_CNN_Intel_Image_Classification.ipynb` top to bottom (Jupyter / VS Code /
Google Colab). This will train the model and save it as `intel_cnn_model.keras` in the same
folder.

### 2. Launch the Streamlit app

Make sure `intel_cnn_model.keras` (produced by step 1) is in the same folder as the app, then:

```bash
streamlit run 1B_streamlit_app.py
```

Upload any scene image (jpg/png) and the app will predict its category with a confidence
score and probability bar chart.

## Notes

- Training was done with `image_dataset_from_directory`, a small data-augmentation pipeline
  (flip/rotate/zoom), and `EarlyStopping` to avoid overfitting.
- Accuracy/loss curves and the confusion matrix are saved as `training_curves.png` and
  `confusion_matrix.png` after running the notebook.
- Possible future improvement: swap the from-scratch CNN for transfer learning
  (MobileNetV2 / ResNet50) to push accuracy higher.
