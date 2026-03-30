# HematoVision

> AI-powered blood cell classification using MobileNetV2 Transfer Learning

Classifies microscopic blood cell images into 4 categories:  
**Eosinophil · Lymphocyte · Monocyte · Neutrophil**

---

## Setup & Run

### 1. Clone the repository

```bash
git clone https://github.com/nanak011/HematoVision
cd HematoVision
```

### 2. Check your Python version

```bash
python --version
```

**Python 3.11 or lower?** → Skip to step 3  
**Python 3.12, 3.13, or 3.14?** → Install Python 3.11 first:

[Download Python 3.11.5 (Windows 64-bit)](https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe)

> During installation check **"Add Python 3.11 to PATH"**

Then create a virtual environment:
```bash
py -3.11 -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install tensorflow flask numpy pillow
```

### 4. Run the app

```bash
python app.py
```

Then open your browser and go to: `http://127.0.0.1:5000`

> The trained model (`blood_cell.h5`) is already included — no extra download needed!

---

## 📁 Project Structure

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

##  Model Details

| Detail | Value |
|---|---|
| Base Model | MobileNetV2 (Transfer Learning) |
| Input Size | 224 × 224 |
| Classes | 4 (Eosinophil, Lymphocyte, Monocyte, Neutrophil) |
| Framework | TensorFlow / Keras |

---

##  Dataset

Dataset sourced from Kaggle:  
[Blood Cell Images – Kaggle](https://www.kaggle.com/datasets/paultimothymooney/blood-cells/data)

> To retrain the model yourself, download the dataset from Kaggle and run `HematoVision_Model.ipynb`

---
Video demosntration:
https://drive.google.com/file/d/1Gm_fNMi2hbPTAsaVb5HICGdNFRYlON_5/view?usp=sharing

## 🛠 Tech Stack

- **Backend:** Python, Flask
- **ML:** TensorFlow, Keras, MobileNetV2
- **Frontend:** HTML, CSS, JavaScript
