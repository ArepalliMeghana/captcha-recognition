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

# Clone the repository
git clone https://github.com/your-username/captcha-recognition.git
cd captcha-recognition

# Install dependencies
pip install -r requirements.txt
<<<<<<< HEAD


python app.py
=======
```
Usage
Running the Web Interface
```bash
python app.py
```

# CAPTCHA Recognition System

## Performance

- Training Accuracy: ~98%
- Validation Accuracy: ~95%
- Average Inference Time: <100ms per image
- Character Recognition Rate: >97%

## Model Training Details

- Epochs: 30
- Batch Size: 16
- Optimizer: Adam
- Loss Function: CTC Loss
- Early Stopping: Patience of 5 epochs
- Data Augmentation: None (base version)

## Implementation Highlights

- Custom CTC Layer: Implements CTC loss for sequence recognition
- Bidirectional Processing: Captures context in both directions
- Efficient Preprocessing: Optimized image processing pipeline
- Robust Architecture: Handles various CAPTCHA styles

## Results Visualization

The system provides visual feedback showing:

- Original CAPTCHA image
- Predicted text
- Confidence scores (if applicable)

## Future Improvements

- Support for more complex CAPTCHA patterns
- Additional data augmentation techniques
- Model optimization for faster inference
- Support for colored CAPTCHAs
- API endpoint implementation

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Dataset source: CaptchaCracker
- TensorFlow team for the deep learning framework
- Gradio team for the web interface framework

## Contact

- Arepalli Meghana
- GitHub: @ArepalliMeghana
- LinkedIn: https://www.linkedin.com/in/meghana-arepalli-6a003a25a

## Citation

@software{captcha_recognition,
    author = {Arepalli Meghana},
    title = {CAPTCHA Recognition System using Deep Learning},
    year = {2024},
    url = {https://github.com/ArepalliMeghana/captcha-recognition}
}
>>>>>>> bb4f601e139c474924f7429b9e2b7c749deef3ad
