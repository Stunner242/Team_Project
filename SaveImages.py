from pymongo import MongoClient  # MongoDB client
import gridfs as gd
from datetime import datetime  # ✅ ADD THIS IMPORT

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")  # MongoDB connection string
db = client["Attendance"]
fs = gd.GridFS(db)

def save_image_to_mongodb(image_path, class_name, subject_name, date_str,stored_id):
    # Open the image file
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

        # Format current date and time
        now = datetime.now()
        readable_time = now.strftime('%Y-%m-%d %I:%M:%S %p')  # e.g., "2025-04-06 02:45:30 PM"

        # Generate a unique filename
        filename = f"{class_name}_{subject_name}_{now.strftime('%Y%m%d%H%M%S')}.jpg"

        # Save image to GridFS with extra 'date' field and present IDs
        fs.put(image_data, filename=filename, metadata={ 
            "Id": stored_id,
            "class_name": class_name,
            "subject_name": subject_name,
            "time": readable_time,
            "date": date_str  # Add today's date in YYYY-MM-DD format
        })

        print(f"✅ Image saved to MongoDB with filename: {filename}")
