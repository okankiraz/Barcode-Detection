from ultralytics import YOLO
from PIL import Image
import os

# 1. Specify the path to the trained model
MODEL_PATH = 'runs/train/barcode_detection4/weights/best.pt'

# 2. Specify the folder containing the images you want to test
IMAGE_PATH = 'img/'

# 3. Specify the folder where the results will be saved
OUTPUT_PATH = 'output/'

# Check if the model and image folder exist
if not os.path.exists(MODEL_PATH):
    print(f"Oops! Model file not found: {MODEL_PATH}")
    exit()
if not os.path.isdir(IMAGE_PATH):
    print(f"Oops! Image folder not found: {IMAGE_PATH}")
    exit()
if not os.path.exists(OUTPUT_PATH):
    os.makedirs(OUTPUT_PATH)

# Load the model
print(f"Loading model: {MODEL_PATH}")
model = YOLO(MODEL_PATH)

# Run predictions on the images
print(f"Running predictions on images in '{IMAGE_PATH}'...")
results = model.predict(source=IMAGE_PATH, conf=0.25, stream=True)

# Process and save the results
print("Processing and saving results...")
for i, result in enumerate(results):
    # Get the original file name
    original_filename = os.path.basename(result.path)
    # Create a new file name for the result
    output_filename = os.path.join(OUTPUT_PATH, f"result_{original_filename}")
    
    print(f"Detected {len(result.boxes)} barcode(s) in: {original_filename}")

    # Save the result (with detected barcodes drawn) to disk
    result.save(filename=output_filename)
    print(f"Result saved successfully to '{output_filename}'")

print("\nAll done! Great job!")