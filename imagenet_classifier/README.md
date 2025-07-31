# ImageNet Classifier

A Python-based image classification system using pre-trained ImageNet models.

## Project Structure

```
imagenet_classifier/
│
├── data/
│   └── test.jpg                 # Your sample input image
│
├── model/
│   └── __init__.py             # Optional init file
│
├── utils/
│   └── image_utils.py          # Image preprocessing and decoding
│
├── main.py                     # Main script to load image and predict
├── requirements.txt            # Required packages
└── README.md                   # Project description
```

## Features

- Support for multiple pre-trained models:
  - MobileNetV2 (default, lightweight)
  - ResNet50 (high accuracy)
  - VGG16 (classic architecture)
  - InceptionV3 (Google's architecture)
- Automatic image preprocessing
- Top-K predictions with confidence scores
- Easy-to-use command-line interface

## Installation

1. Clone or download this project
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```bash
python main.py --image data/test.jpg
```

### Advanced Usage

```bash
# Use ResNet50 model
python main.py --image data/test.jpg --model resnet50

# Show top 10 predictions
python main.py --image data/test.jpg --top-k 10

# Combine options
python main.py --image data/test.jpg --model vgg16 --top-k 3
```

### Command Line Arguments

- `--image` / `-i`: Path to input image (required)
- `--model` / `-m`: Model to use (default: mobilenet_v2)
  - Options: `mobilenet_v2`, `resnet50`, `vgg16`, `inception_v3`
- `--top-k` / `-k`: Number of top predictions to show (default: 5)

## Supported Image Formats

- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)
- TIFF (.tiff)
- And other formats supported by PIL

## Example Output

```
Loading mobilenet_v2 model...
Model mobilenet_v2 loaded successfully!
Making prediction for: data/test.jpg

Top predictions:
--------------------------------------------------
1. Egyptian_cat: 0.8547 (85.47%)
2. tabby: 0.1123 (11.23%)
3. tiger_cat: 0.0231 (2.31%)
4. lynx: 0.0045 (0.45%)
5. Siamese_cat: 0.0032 (0.32%)
```

## Model Information

### MobileNetV2
- **Pros**: Fast inference, small model size
- **Cons**: Slightly lower accuracy
- **Best for**: Real-time applications, mobile deployment

### ResNet50
- **Pros**: High accuracy, good balance
- **Cons**: Larger model size
- **Best for**: High accuracy requirements

### VGG16
- **Pros**: Simple architecture, good interpretability
- **Cons**: Large model size, slower inference
- **Best for**: Educational purposes, feature extraction

### InceptionV3
- **Pros**: Good accuracy, efficient architecture
- **Cons**: More complex preprocessing
- **Best for**: Advanced classification tasks

## Requirements

- Python 3.7+
- TensorFlow 2.10+
- See `requirements.txt` for complete list

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this classifier.
