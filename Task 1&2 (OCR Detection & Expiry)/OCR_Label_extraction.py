import google.generativeai as genai
import time
import os
from paddleocr import PaddleOCR, draw_ocr

os.environ['GOOGLE_API_KEY'] = 'AIzaSyCiLVasyxqKMP3qMcJLXdqu33XyTNDqK1M'
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

gemini_model = genai.GenerativeModel('gemini-1.5-flash')

# Initializing OCR, OCR will automatically download PP-OCRv3 detector, recognizer and angle classifier.
ocr = PaddleOCR(use_angle_cls=True, lang='en', det_model_dir='./models/det', rec_model_dir='./models/rec', cls_model_dir='./models/cls', use_gpu=False)  # Set use_gpu=False to use CPU

def generate_answer(img_path):
    start = time.time()
    result = ocr.ocr(img_path)

    text_data = "\n".join([item[-1][0] for item in result[0]])

    # Prompt for the Gemini model, incorporating more specific questions and field names
    prompt = f"""
    Extract the following information from the text:

    - **brand_name:** The name of the brand or company
    - **product_name:** The specific name of the food item
    - **product_type:** The general category of the food item (e.g., snack, beverage, dairy)
    - **ingredients:** A list of ingredients with their quantities in grams
    - **nutrition_facts:** Nutritional information, including calories, fat, carbohydrates, protein, etc.
    - **manufacturing_date:** The date the product was manufactured
    - **expiration_date:** The expiration date of the product
    - **price:** The price of the product
    - **barcode:** The product's barcode (if available)

    Provide the extracted information in a well-formatted text format.

    Text:
    {text_data}
    """

    try:
        gemini_response = gemini_model.generate_content(prompt)
        print("\nExtracted Information:")
        print(gemini_response.text)

        end = time.time()
        print(f"Time elapsed: {end - start:.2f} seconds")

    except Exception as e:
        if isinstance(e, json.JSONDecodeError):
            print(f"Error occurred: Invalid JSON data: {e}")
        else:
            print(f"Error occurred: {e}")

# Example usage
img_path = "handwash.jpeg"
generate_answer(img_path)