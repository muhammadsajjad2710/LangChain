import google.generativeai as genai
from PIL import Image
import os
import json

# Set up Gemini API key
genai.configure(api_key="AIzaSyBpL9c4jjBmRnWviTVjDNTLjhAGmcqfUa4")

# Path to the handwritten image
image_path = "C:Users\DELL\Downloads/images.jfif"

# Check if the file exists
if not os.path.exists(image_path):
    print("Error: Image file not found.")
    exit()

# Load the image
image = Image.open(image_path)

# Initialize Gemini model (Gemini 2 Vision)
model = genai.GenerativeModel("gemini-1.5-flash")

# Generate response from the model
response = model.generate_content([image, "Extract the handwritten text from this image."])

# Get the extracted text
if response.text:
    extracted_text = response.text.strip()
    print("\nExtracted Handwritten Text:\n", extracted_text)

    # Save output in JSON format
    output_data = {"handwritten_text": extracted_text}

    json_file_path = "handwritten_output.json"
    with open(json_file_path, "w", encoding="utf-8") as json_file:
        json.dump(output_data, json_file, ensure_ascii=False, indent=4)

    print(f"Output saved to {json_file_path}")
else:
    print("No text extracted from the image.")
