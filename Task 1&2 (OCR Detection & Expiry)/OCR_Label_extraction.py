import google.generativeai as genai
import time
import os
import json
from paddleocr import PaddleOCR, draw_ocr

os.environ['GOOGLE_API_KEY'] = 'AIzaSyCiLVasyxqKMP3qMcJLXdqu33XyTNDqK1M'
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

gemini_model = genai.GenerativeModel('gemini-1.5-flash')


# Initializing OCR, OCR will automatically download PP-OCRv3 detector, recognizer and angle classifier.
ocr = PaddleOCR(use_angle_cls=True)

def generate_answer(img_path, output_file='output.json'):
    start = time.time()
    result = ocr.ocr(img_path)

    text_data = "\n".join([item[-1][0] for item in result[0]])

    # Prompt for the Gemini model, incorporating more specific questions and field names
    prompt = f"""
    Extract the following information from the text:

    - **brand_name:** The name of the brand or company
    - **product_type:** The type of food or product
    - **ingredients:** A list of ingredients with their quantities in grams
    - **manufacturing_date:** The date the product was manufactured
    - **price:** The price of the product
    - **expiry_date:** The expiration date of the product

    Provide the extracted information in a JSON format.

    Text:
    {text_data}
    """

    gemini_response = gemini_model.generate_content(prompt)
    json_data = json.loads(gemini_response.text)

    # Add more fields or modify existing fields as needed
    json_data['image_path'] = img_path

    with open(output_file, 'w') as f:
        json.dump(json_data, f, indent=4)

    end = time.time()
    print(f"Output saved to {output_file}")
    print(f"Time elapsed: {end - start:.2f} seconds")

# Example usage
img_path = "/content/WhatsApp Image 2024-10-16 at 20.18.23.jpeg"
generate_answer(img_path)