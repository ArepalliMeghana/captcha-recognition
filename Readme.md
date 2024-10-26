# CAPTCHA Recognition System using Deep Learning

## Overview
This project implements a deep learning model for recognizing text in CAPTCHA images using a combination of Convolutional Neural Networks (CNN) and Recurrent Neural Networks (RNN). The system achieves high accuracy in decoding CAPTCHAs through a sophisticated architecture that combines image processing and sequence recognition.

## Key Features
- **Advanced Architecture**: Combines CNN for feature extraction and Bidirectional LSTM for sequence processing
- **CTC Loss Implementation**: Uses Custom CTC (Connectionist Temporal Classification) layer for efficient text recognition
- **User-friendly Interface**: Web-based interface built with Gradio for easy testing
- **High Accuracy**: Achieves reliable recognition rates on various CAPTCHA formats
- **Real-time Processing**: Quick response time for immediate results

## Technical Details

### Model Architecture
1. **Input Layer**: Accepts grayscale images (200x50 pixels)
2. **Convolutional Layers**:
   - First Conv Block: 32 filters with 3x3 kernel + MaxPooling
   - Second Conv Block: 64 filters with 3x3 kernel + MaxPooling
3. **Dense Layer**: 64 units with ReLU activation
4. **Bidirectional LSTM Layers**:
   - First LSTM: 128 units (bidirectional)
   - Second LSTM: 64 units (bidirectional)
5. **Output Layer**: Dense layer with softmax activation
6. **CTC Layer**: Custom implementation for sequence recognition

### Dataset
- Training set: 1040 CAPTCHA images
- Image dimensions: 200x50 pixels
- Character set: 19 unique characters (digits and lowercase letters)
- Maximum text length: 5 characters

## Installation

### Prerequisites
- Python 3.10 or higher
- TensorFlow 2.x
- CUDA-capable GPU (recommended)

### Setup
```bash
# Clone the repository
git clone https://github.com/your-username/captcha-recognition.git
cd captcha-recognition

# Install dependencies
pip install -r requirements.txt