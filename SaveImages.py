from pymongo import MongoClient # MongoDB client
from PIL import Image
import gridfs as gd
from datetime import datetime
import cv2

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")  # MongoDB connection string
db = client["Attendance"]
fs = gd.GridFS(db)

def save_image_to_mongodb(image_path, class_name, subject_name):
    # Open the image file
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

        # Format current date and time
        now = datetime.now()
        readable_time = now.strftime('%Y-%m-%d %I:%M:%S %p')  # e.g., "2025-04-06 02:45:30 PM"

        # Generate a unique filename
        filename = f"{class_name}_{subject_name}_{now.strftime('%Y%m%d%H%M%S')}.jpg"

        # Save image to GridFS with metadata
        fs.put(image_data, filename=filename, metadata={
            "class_name": class_name,
            "subject_name": subject_name,   # subject name
            "time": readable_time               # human-friendly time
        })

        print(f"✅ Image saved to MongoDB with filename: {filename}")
