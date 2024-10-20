
# Flipkart Grid 6.0 Hackathon Project

This repository contains the project submission for the *Flipkart Grid 4.0 Hackathon*. The project aims to solve real-world challenges in the retail and FMCG (Fast-Moving Consumer Goods) industry using cutting-edge technology such as OCR (Optical Character Recognition), image recognition, and machine learning models for product identification, expiry validation, and freshness detection.



## Technical Stack

- *OCR*: [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) or other OCR engines for text extraction from images.
- *Machine Learning*: Image recognition models (e.g. TensorFlow, PyTorch) for detecting product brands and shelf-life prediction.
- *Infrared Technology*: IR-based recognition for count validation.
- *Data Processing*: Python for data processing and integration with OCR/ML models.

  
## Task 1 and Task 2 - OCR & Expiry Date Extraction
These scripts leverage Optical Character Recognition (OCR) and generative AI models to identify product details from images and extract expiration date information from labels.

### Task 1: OCR to Extract Product Details
- **Objective**: Extract important product information like brand name, product type, ingredients, manufacturing date, and expiry date using OCR and an advanced language model (Gemini).
- **Key Features**:
  - Utilize PaddleOCR for text extraction from product images.
  - Send the extracted text to the **Gemini** model for advanced natural language processing to identify specific fields like brand, price, and expiration date.
  
### Task 2: OCR for Expiry Date Validation
- **Objective**: Extract and validate expiry dates from product labels using OCR and regular expressions.
- **Key Features**:
  - Detect objects on product labels using a Roboflow inference model.
  - Extract expiry dates from the detected objects using `pytesseract`.
  - Validate the detected expiry dates using pattern matching (e.g., MM/DD/YYYY format).

### Prerequisites
- Python 3.7 or higher
- Install necessary libraries:
    - `cv2` (OpenCV)
    - `pytesseract`
    - `pillow`
    - `paddleocr`
    - `requests`
    - `google-generativeai`
    - `inference_sdk`
## Task 3: Brand Logo Detection

This task is centered around detecting brand logos in images using **YOLOv8**. The detection process is executed through a Python script called `main_detection_yolov8.py`. By running this script with specified parameters (such as the model and input image), the system processes the image and saves the detection results in a predefined results directory.

### Inference Process

By running the detection script, users can utilize **YOLOv8** to detect logos on input images. The model scans the image, and identifies, and localizes brand logos, demonstrating accuracy in varied scenarios.


## Task 4: Detecting Freshness of Fresh Produce
- **Objective**: Detect fresh produce items in a live video feed and predict their freshness or credibility score.
- **Approach**:
  - **YOLOv8** is used for object detection to identify produce (e.g., bananas, apples) in the camera feed.
  - **AlexNet** is used to analyze the detected items and compute a credibility score, which correlates to the freshness or quality of the produce.
- **Key Features**:
  - Real-time object detection using **YOLOv8**.
  - Freshness/credibility score prediction using a fine-tuned **AlexNet** model.
  - Bounding boxes and the corresponding credibility scores are displayed on the video feed in real-time.

## Installation

### Prerequisites
Ensure you have the following dependencies installed:
- **Python 3.7+**
- **PyTorch** for loading the AlexNet model and performing inference.
- **OpenCV** for capturing video frames and drawing bounding boxes.
- **Ultralytics YOLO** for object detection using YOLOv8.
- **PIL (Python Imaging Library)** for image processing and handling.
- **Torchvision** for model transformations.
  

