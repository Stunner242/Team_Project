from pymongo import MongoClient
import gridfs
from datetime import datetime

client = MongoClient("mongodb://localhost:27017")
db = client["Attendance"]  # Connect to the database
fs = gridfs.GridFS(db)     # Initialize GridFS

def get_image(class_name, subject_name):
    # Get today’s date string (same format as saved in metadata)
    today_date = datetime.now().strftime('%Y-%m-%d')

    query = {}
    if class_name:
        query["metadata.class_name"] = class_name
    if subject_name:
        query["metadata.subject_name"] = subject_name

    # ✅ Add date filter: only today's images
    query["metadata.date"] = today_date

    images = db.fs.files.find(query)
    image_list = []
    for file in images: # file is a dictionary containing metadata and 
        metadata = file.get("metadata", {})
        image_list.append({
            "id": str(file["_id"]),
            "filename": file["filename"],
            "class_name": metadata.get("class_name", ""),
            "subject_name": metadata.get("subject_name", ""),
            "time": metadata.get("time", ""),
            "set_id": metadata.get("Id", "")
        })

    return image_list
