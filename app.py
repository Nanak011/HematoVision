from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

# Load the trained model
MODEL_PATH = r"D:\HematoVision\blood_cell.h5"
model = load_model(MODEL_PATH)
print("✅ Model loaded successfully!")

# Class names — must match the order from training
CLASS_NAMES = ['EOSINOPHIL', 'LYMPHOCYTE', 'MONOCYTE', 'NEUTROPHIL']

# Folder to temporarily save uploaded images
UPLOAD_FOLDER = r"D:\HematoVision\static\uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return "No file uploaded", 400

    file = request.files['image']

    if file.filename == '':
        return "No file selected", 400

    # Save the uploaded image
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # Prepare the image for the model
    img = image.load_img(filepath, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    # Predict
    predictions = model.predict(img_array)
    predicted_index = np.argmax(predictions[0])
    predicted_class = CLASS_NAMES[predicted_index]
    confidence = round(float(np.max(predictions[0])) * 100, 2)

    # Pass result to result page
    img_display_path = '/static/uploads/' + file.filename

    return render_template(
        'result.html',
        prediction=predicted_class,
        confidence=confidence,
        img_path=img_display_path
    )


if __name__ == '__main__':
    app.run(debug=True)
