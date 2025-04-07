from pymongo import MongoClient
import gridfs
from PIL import Image
import io

client = MongoClient("mongodb://localhost:27017")
db = client["Attendance"] # Connect to the database
fs = gridfs.GridFS(db) # Initialize GridFS
def get_image(class_name, subject_name):
    query = {}
    if class_name:
        query["metadata.class_name"] = class_name # Filter by class name
    if subject_name:
        query["metadata.subject_name"] = subject_name  # Filter by subject name
    
    images = db.fs.files.find(query)
    image_list = []
    for file in images: # Get the file metadata
        print("Found file:", file["filename"]) 
        metadata = file.get("metadata", {})
        image_list.append({
            "id": str(file["_id"]),
            "filename": file["filename"],
            "class_name": metadata.get("class_name", ""),
            "subject_name": metadata.get("subject_name", ""),
            "time": metadata.get("time", "")
        })

    return image_list # Return the list of images with metadata
    


