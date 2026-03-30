# HematoVision

> AI-powered blood cell classification using MobileNetV2 Transfer Learning

Classifies microscopic blood cell images into 4 categories:  
**Eosinophil · Lymphocyte · Monocyte · Neutrophil**

## Setup & Run

### 1. Clone the repo

```bash
git clone https://github.com/nanak011/HematoVision.git
cd HematoVision
```

### 2. Install dependencies

```bash
pip install tensorflow flask numpy pillow
```

### 3. Run the app

```bash
python app.py
```

Then open your browser and go to: `http://127.0.0.1:5000`

> The trained model (`blood_cell.h5`) is already included — no extra download needed!

---

## Project Structure

```
HematoVision/
│
├── static/
│   └── uploads/                  ← uploaded images saved here temporarily
│
├── templates/
│   ├── home.html                 ← upload page
│   └── result.html               ← result page
│
├── app.py                        ← Flask backend
├── blood_cell.h5                 ← pre-trained model
├── HematoVision_Model.ipynb      ← model training notebook
├── readme.md
└── .gitignore
```

---

## Model Details

| Detail | Value |
|---|---|
| Base Model | MobileNetV2 (Transfer Learning) |
| Input Size | 224 × 224 |
| Classes | 4 (Eosinophil, Lymphocyte, Monocyte, Neutrophil) |
| Framework | TensorFlow / Keras |

---

## Dataset

Dataset sourced from Kaggle:  
👉 [Blood Cell Images – Kaggle](https://www.kaggle.com/datasets/paultimothymooney/blood-cells/data)

> To retrain the model yourself, download the dataset from Kaggle and run `HematoVision_Model.ipynb`

---

## Tech Stack

- **Backend:** Python, Flask
- **ML:** TensorFlow, Keras, MobileNetV2
- **Frontend:** HTML, CSS, JavaScript
