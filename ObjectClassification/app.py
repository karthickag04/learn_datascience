# MobileNetV2 Image Classification with Flask
# ===========================================
# MobileNetV2 is a powerful, lightweight model designed to run efficiently on mobile and edge devices. It is particularly popular for applications requiring real-time object detection, image classification, and other computer vision tasks, especially where computational resources are limited.


from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)
model = MobileNetV2(weights='imagenet')  # Load pre-trained MobileNetV2

def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = model.predict(x)
    return decode_predictions(preds, top=1)[0][0]

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"})
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join('uploads', filename)
        file.save(file_path)
        result = model_predict(file_path, model)
        return jsonify({"result": result[1]})

if __name__ == '__main__':
    app.run(debug=True)
