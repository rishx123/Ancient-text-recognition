import pytesseract
from PIL import Image
import numpy as np
import cv2

# Set the correct Tesseract-OCR path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def preprocess_image(image):
    """Enhances image quality for better OCR accuracy."""
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    processed = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
    )
    return processed

def extract_text(image):
    """Runs OCR on the processed image and returns extracted text."""
    pil_image = Image.fromarray(image)
    text = pytesseract.image_to_string(pil_image)
    return text  # ✅ Returns the extracted text correctly
