import os
from tensorflow.keras.applications.resnet50 import ResNet50, decode_predictions
from utils.image_utils import load_and_preprocess_image

def main():
    # Load ResNet50 pretrained on ImageNet
    model = ResNet50(weights='imagenet')

    # Load and preprocess image
    img_path = 'data/test.jpg'  # <-- Make sure image exists
    if not os.path.exists(img_path):
        print(f"Image not found: {img_path}")
        return

    x = load_and_preprocess_image(img_path)

    # Predict
    preds = model.predict(x)

    # Decode top 3 predictions
    results = decode_predictions(preds, top=3)[0]
    print("Predictions:")
    for (_, label, prob) in results:
        print(f"{label}: {prob*100:.2f}%")

if __name__ == "__main__":
    main()
