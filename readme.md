HematoVision

AI-powered blood cell classification using MobileNetV2 Transfer Learning

Classifies microscopic blood cell images into 4 categories:
Eosinophil · Lymphocyte · Monocyte · Neutrophil

Setup & Run
1. Clone the repo
bashgit clone https://github.com/YOUR_USERNAME/HematoVision.git
cd HematoVision
2. Install dependencies
pip install tensorflow flask numpy pillow
3. Run the app
python app.py
Then open your browser and go to: http://127.0.0.1:5000


The trained model (blood_cell.h5) is already included — no extra download needed!


📁 Project Structure
HematoVision/
│
├── static/
│   └── uploads/          ← uploaded images saved here temporarily
│
├── templates/
│   ├── home.html         ← upload page
│   └── result.html       ← result page
│
├── app.py                ← Flask backend
├── HematoVision_Model.ipynb  ← model training notebook
├── readme.md
└── .gitignore

Model Details
DetailValueBase ModelMobileNetV2 (Transfer Learning)Input Size224 × 224Classes4 (Eosinophil, Lymphocyte, Monocyte, Neutrophil)FrameworkTensorFlow / Keras

Dataset
Dataset sourced from Kaggle:
https://www.kaggle.com/datasets/paultimothymooney/blood-cells/data

Tech Stack

Backend: Python, Flask
ML: TensorFlow, Keras, MobileNetV2
Frontend: HTML, CSS, JavaScript
