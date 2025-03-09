from fastapi import FastAPI, File, UploadFile
import pytesseract
from PIL import Image
import cv2
import numpy as np
import io

app = FastAPI()

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

@app.post("/upload/")  # ✅ Ensure it's POST
async def upload_image(file: UploadFile = File(...)):
    contents = await file.read()
    image = np.array(Image.open(io.BytesIO(contents)))
    
    # Convert to grayscale and apply thresholding
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    processed = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    text = pytesseract.image_to_string(Image.fromarray(processed))

    return {"extracted_text": text}
