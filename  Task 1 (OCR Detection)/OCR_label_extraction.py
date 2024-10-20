# Import necessary libraries
import cv2
import requests
from PIL import Image
import pytesseract
import re
import google.generativeai as genai
from inference_sdk import InferenceHTTPClient

# Step 1: Configure the Inference Client
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="B739AZZ5Ga3sgjGztVI1"
)

# Step 2: Configure the API Key for Gemini
genai.configure(api_key="AIzaSyBW8UrfLMN3blHpSElVlbDFuzleecYMDnA")  # Your API key

# Function to extract text using OCR
def perform_ocr(image):
    gray_image = image.convert('L')  # Convert to grayscale
    return pytesseract.image_to_string(gray_image, config='--psm 6')

# Function to analyze the extracted text using Gemini
def analyze_text_with_gemini(extracted_text):
    prompt = f"""
    Analyze the following text and identify the product information including:
    - Product Name
    - Product Description
    - Serial Number (EAN)
    - Label
    - MRP (Maximum Retail Price)
    ...
    Text: {extracted_text}
    """
    # Generate response from Gemini model
    model = genai.GenerativeModel(
        model_name="gemini-pro",
        safety_settings=[],
        generation_config={"temperature": 0, "top_p": 1, "top_k": 1, "max_output_tokens": 4096}
    )
    response = model.generate_content(prompt)
    return response.text

# Step 3: Initialize camera capture
cap = cv2.VideoCapture(0)  # 0 for default camera

while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to RGB (OpenCV uses BGR by default)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Step 4: Save the frame temporarily to a file for inference
    temp_image_path = 'temp_frame.jpg'  # Path to save the temporary image
    cv2.imwrite(temp_image_path, rgb_frame)

    # Perform object detection using the inference model
    result = CLIENT.infer(temp_image_path, model_id="flipkartgrid-ocr-tmd6q-lbde9/1")

    # Step 5: Loop through all predictions and process detected regions
    for idx, detection in enumerate(result['predictions']):
        x, y, width, height = detection['x'], detection['y'], detection['width'], detection['height']

        # Calculate bounding box coordinates
        left = int(x - width / 2)
        top = int(y - height / 2)
        right = int(x + width / 2)
        bottom = int(y + height / 2)

        # Crop the detected region from the frame
        cropped_frame = frame[top:bottom, left:right]
        cropped_img = Image.fromarray(cv2.cvtColor(cropped_frame, cv2.COLOR_BGR2RGB))

        # Perform OCR on the cropped image
        expiry_date_text = perform_ocr(cropped_img)
        print(f"Detected Expiry Date Text for Detection {idx + 1}: {expiry_date_text}")

        # Post-process the OCR output to extract a valid date
        date_pattern = r'\b(0?[1-9]|1[0-2])[/\-](0?[1-9]|[12][0-9]|3[01])[/\-]((19|20)\d\d)\b'
        match = re.search(date_pattern, expiry_date_text)

        if match:
            print(f"Expiry Date for Detection {idx + 1}: {match.group()}")
        else:
            print(f"No valid date found for Detection {idx + 1}.")

        # Analyze extracted text using Gemini
        analysis_result = analyze_text_with_gemini(expiry_date_text)
        print("Analysis Result:")
        print(analysis_result)

    # Show the frame with bounding boxes (optional)
    cv2.imshow('Object Detection', frame)

    # Exit loop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()
