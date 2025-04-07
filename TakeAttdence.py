from Match import generate_face_encodings_from_image
from SaveImages import save_image_to_mongodb  # ✅ Import image saver
import cv2
import os
import time

def capture_images(class_name, subject_name):
    desktop_path = r"C:\Users\Lenovo\OneDrive\Desktop\307"
    os.makedirs(desktop_path, exist_ok=True)

    # Initialize webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        return "Error: Could not open webcam."

    while True:
        ret, frame = cap.read()
        if not ret:
            return "Error: Could not capture frame from webcam."

        cv2.imshow("Capture Window", frame)

        # Capture image on spacebar press
        if cv2.waitKey(1) & 0xFF == ord(' '):
            # Save image locally first
            filename = f"captured_image_{int(time.time())}.jpg"
            filepath = os.path.join(desktop_path, filename)
            cv2.imwrite(filepath, frame)
            print(f"✅ Image saved locally to: {filepath}")

            # Save image to MongoDB using the separate module
            save_image_to_mongodb(filepath, class_name, subject_name)

            # Generate face encodings (optional)
            generate_face_encodings_from_image(filepath, class_name, subject_name)

        # Exit on 'q' press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return "Image capture session ended."
