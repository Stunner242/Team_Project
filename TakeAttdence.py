from Match import generate_face_encodings_from_image  # ✅ Import face encoding generation
from SaveImages import save_image_to_mongodb  # ✅ Import image saver
import cv2
import os
import time
from datetime import datetime
from pymongo import MongoClient
import gridfs
from updateabsent import update_absent

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")  # MongoDB connection string
db = client["Attendance"]
fs = gridfs.GridFS(db)

def capture_images(class_name, subject_name):
    desktop_path = r"C:\Users\Lenovo\OneDrive\Desktop\307"  # Path where captured images are saved locally
    os.makedirs(desktop_path, exist_ok=True)  # Create directory if not exists

    # Initialize webcam
    cap = cv2.VideoCapture(0)  # Open the webcam
    all_present_ids = set()  # To keep track of all present students' IDs

    if not cap.isOpened():  # Check if the webcam is successfully opened
        return "Error: Could not open webcam."

    while True:
        ret, frame = cap.read()  # Capture frame from the webcam
        if not ret:  # If frame capture failed
            return "Error: Could not capture frame from webcam."

        cv2.imshow("Capture Window", frame)  # Display the captured frame in a window

        # Capture image on spacebar press
        if cv2.waitKey(1) & 0xFF == ord(' '):
            # Save image locally first
            filename = f"captured_image_{int(time.time())}.jpg"
            filepath = os.path.join(desktop_path, filename)
            cv2.imwrite(filepath, frame)  # Save the captured frame as an image
            print(f"✅ Image saved locally to: {filepath}")

            # Get today's date
            today_date = datetime.now().strftime('%Y-%m-%d')

            # Generate face encodings and get attendance messages
            attendance_messages,present_ids,stored_id = generate_face_encodings_from_image(filepath, class_name, subject_name)

            # Check if any message indicates successful attendance marking
            marked = any(msg.startswith(" Attendance marked") for msg in attendance_messages)

            # Annotate the frame with attendance messages
            display_frame = frame.copy()
            y_offset = 30  # Starting vertical position
            for message in attendance_messages:
                cv2.putText(display_frame, message, (10, y_offset),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                y_offset += 30  # Move down for the next line

            if marked:
                print("✅ Attendance marked — saving image to MongoDB.")
                # Save raw image to MongoDB
                # save_image_to_mongodb(filepath, class_name, subject_name, today_date)

                # Add recognized IDs to the set of present IDs
                all_present_ids.update(present_ids)

                # Save annotated image with attendance messages to MongoDB
                annotated_filename = f"annotated_{int(time.time())}.jpg"
                annotated_filepath = os.path.join(desktop_path, annotated_filename)
                cv2.imwrite(annotated_filepath, display_frame)
                save_image_to_mongodb(annotated_filepath, class_name, subject_name, today_date,stored_id)
            else:
                print("❌ No attendance marked — not saving this image to MongoDB.")

            # Show the updated frame with messages
            cv2.imshow("Capture Window", display_frame)
            cv2.waitKey(2000)  # Wait 2 seconds so user can read the message

        # Exit on 'q' press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()  # Release the webcam
    cv2.destroyAllWindows()  # Close all OpenCV windows

    # Update the attendance status for present students
    update_absent(list(all_present_ids), class_name, subject_name)
    return "Image capture session ended."
