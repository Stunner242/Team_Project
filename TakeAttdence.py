from Match import generate_face_encodings_from_image
import cv2
import os
import time
def capture_images():
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
            filename = f"captured_image_{int(time.time())}.jpg"
            filepath = os.path.join(desktop_path, filename)
            cv2.imwrite(filepath, frame)
            print(f"Image saved successfully to: {filepath}")
            generate_face_encodings_from_image(filepath)


        # Exit on 'q' press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release() 
    cv2.destroyAllWindows()
    return "Image capture session ended."