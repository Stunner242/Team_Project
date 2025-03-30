import face_recognition
import cv2
import os
import time
from EncodingSave import saveEncoding
from flask import Flask, request, render_template
from StudentDatasave import saveStudentData

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('Student.html')

 # Call the capture_images function to start capturing images
@app.route('/Next_Student')
def take_attendance():
    return render_template('Student.html')  
@app.route('/Stop_Server')
def stop_server():
    return "Server Stopped"
@app.route('/start', methods=['POST'])
def start():
    name=request.form['name']
    roll_no=request.form['Roll_no']
    id=request.form['id']
    gender=request.form['Gender']
    class1=request.form['class']
    password=request.form['password']
    saveStudentData(id,name,password,gender,class1,roll_no)
    print("Student Data Saved")
    image_path = capture_images()
    encodings=generate_face_encodings_from_image(image_path)
    if encodings:
        saveEncoding(encodings, name, roll_no, id)
        return render_template('Admin.html')
    else:
        return "Error: No face detected in the image."



def capture_images():
    desktop_path = r"C:\Users\Lenovo\OneDrive\Desktop\307"
    os.makedirs(desktop_path, exist_ok=True)

    # Initialize webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return None

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not capture frame from webcam.")
            break

        cv2.imshow("Capture Window", frame)

        # Capture image on spacebar press
        key = cv2.waitKey(1) & 0xFF
        if key == ord(' '):  # Spacebar key
            filename = f"captured_image_{int(time.time())}.jpg"
            filepath = os.path.join(desktop_path, filename)
            cv2.imwrite(filepath, frame)
            print(f"Image saved successfully to: {filepath}")
            break  # Exit after capturing image

        # Exit on 'q' press
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    
    return filepath if 'filepath' in locals() else None

def generate_face_encodings_from_image(image_path):
    """Generates face encodings for all faces in an image and displays detected faces."""

    if image_path is None:
        print("Error: No image captured.")
        return []

    # Read the image using OpenCV
    image = cv2.imread(image_path)
    
    if image is None:
        print("Error loading image.")
        return []

    print(f"Image shape: {image.shape}, dtype: {image.dtype}")

    # Convert image to RGB (required by face_recognition)
    try:
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    except Exception as e:
        print(f"Error converting image to RGB: {e}")
        return []

    # Detect faces in the image
    face_locations = face_recognition.face_locations(rgb_image)

    if not face_locations:
        print("No faces found in the image.")
        return []

    # Encode each detected face and draw a rectangle
    face_encodings = []
    for face_location in face_locations:
        encoding = face_recognition.face_encodings(rgb_image, [face_location])[0]
        face_encodings.append(encoding)

        # Draw a rectangle around the detected face
        top, right, bottom, left = face_location
        cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)

    # Show the image with detected faces
    cv2.imshow("Detected Faces", image)
    cv2.waitKey(0)  # Wait for a key press
    cv2.destroyAllWindows()  # Close the window

    return face_encodings
if __name__ == '__main__':
    app.run(debug=True)