!pip install numpy pandas matplotlib seaborn tensorflow keras opencv-python

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = "C:/Users/Rishitha SJ/Downloads/dataset/ins1/IMG_3917.jpg"  # Change to your image path
image = cv2.imread(image_path)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply adaptive thresholding (better for uneven lighting)
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Apply edge detection (Canny)
edges = cv2.Canny(thresh, 50, 100)

# Resize image for uniform processing
resized = cv2.resize(thresh, (500, 500))  # Adjust size as needed

# Display results
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.imshow(gray, cmap="gray")
plt.title("Grayscale Image")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(thresh, cmap="gray")
plt.title("Thresholded Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(edges, cmap="gray")
plt.title("Edge Detection")
plt.axis("off")

plt.show()


import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = "C:/Users/Rishitha SJ/Downloads/dataset/ins1/IMG_3917.jpg"
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB for correct display

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply adaptive thresholding (Improved version)
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                               cv2.THRESH_BINARY_INV, 21, 9)

# Find contours for text segmentation
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw bounding boxes on the original image
image_with_boxes = image.copy()
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    if w > 10 and h > 10:  # Filter small noise
        cv2.rectangle(image_with_boxes, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green box

# Plot the results
plt.figure(figsize=(10, 5))

# Show the improved thresholded image
plt.subplot(1, 2, 1)
plt.imshow(thresh, cmap="gray")
plt.title("Improved Thresholded Image")
plt.axis("off")

# Show the image with bounding boxes
plt.subplot(1, 2, 2)
plt.imshow(image_with_boxes)
plt.title("Text Segmentation (Bounding Boxes)")
plt.axis("off")

plt.show()


import numpy as np

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to extract text
_, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)

# Show processed image
plt.imshow(binary, cmap="gray")
plt.axis("off")
plt.show()

import cv2
import numpy as np
import pytesseract

def preprocess_for_ocr(image):
    # Ensure image is grayscale
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image

    # Apply Gaussian Blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    # Use adaptive thresholding for better results
    binary = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY, 11, 2)

    # Dilation to enhance character strokes
    kernel = np.ones((2,2), np.uint8)
    processed = cv2.dilate(binary, kernel, iterations=1)

    return processed

def recognize_characters(char_images):
    recognized_text = []
    
    for i, char_img in enumerate(char_images[:5]):  # Process only first 5 characters for testing
        processed_img = preprocess_for_ocr(char_img)  # Apply preprocessing
        text = pytesseract.image_to_string(processed_img, config='--psm 10 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')
        text = text.strip().replace("\n", "")  # Remove extra whitespace
        print(f"Character {i+1}: '{text}'")  # Display recognized character
        recognized_text.append(text)

    return recognized_text

# Assuming `char_images` contains segmented character images
extracted_text = recognize_characters(char_images)

print("Recognized Characters:", extracted_text)



pip install googletrans==4.0.0-rc1 --no-deps
 from googletrans import Translator

# Function to clean and join extracted characters
def clean_and_combine_text(recognized_text):
    cleaned_text = [char for char in recognized_text if char.isalnum()]  # Remove unwanted symbols
    combined_text = "".join(cleaned_text)  # Merge characters into words
    return combined_text

# Function to translate text using Google Translate
def translate_text(text, target_lang="en"):  # 'en' for English, 'hi' for Hindi
    translator = Translator()
    translated = translator.translate(text, dest=target_lang)
    return translated.text

# Clean and combine recognized characters into words
final_text = clean_and_combine_text(extracted_text)

# Translate to English
translated_text = translate_text(final_text, target_lang="en")

print("Final Recognized Text:", final_text)
print("Translated Text:", translated_text)

pip install textblob
from textblob import TextBlob

def correct_text(text):
    return str(TextBlob(text).correct())

corrected_text = correct_text(final_text)
print("Corrected Text:", corrected_text)


# Clean, correct, filter, and translate
final_text = clean_and_combine_text(extracted_text)
corrected_text = correct_text(final_text)
filtered_text = filter_text(corrected_text)
translated_text = translate_text(filtered_text, target_language='en')

print("Final Translated Text:", translated_text)





