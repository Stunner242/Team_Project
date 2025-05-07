import face_recognition
import cv2
import os
import time
from EncodingSave import saveEncoding
from StudentDatasave import saveStudentData
from flask import render_template, request

def process_student_registration():
    name = request.form['name']
    roll_no = request.form['Roll_no']
    id = request.form['id']
    gender = request.form['Gender']
    class1 = request.form['class']
    password = request.form['password']
    Email = request.form['email']
    phone = request.form['phone']

    saveStudentData(id, name, password, gender, class1, roll_no,Email,phone)
    print("Student Data Saved")

    image_path = capture_images()
    encodings = generate_face_encodings_from_image(image_path)

    if encodings:
        saveEncoding(encodings, name, roll_no, id)
        return render_template('Admin.html', username='Admin')  # Pass username to template
    else:
        return "Error: No face detected in the image."

def capture_images():
    desktop_path = r"C:\Users\Lenovo\OneDrive\Desktop\307"
    os.makedirs(desktop_path, exist_ok=True)

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return None

    filepath = None
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not capture frame from webcam.")
            break

        cv2.imshow("Capture Window", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord(' '):  # Spacebar key
            filename = f"captured_image_{int(time.time())}.jpg"
            filepath = os.path.join(desktop_path, filename)
            cv2.imwrite(filepath, frame)
            print(f"Image saved successfully to: {filepath}")
            break

        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return filepath

def generate_face_encodings_from_image(image_path):
    if image_path is None:
        print("Error: No image captured.")
        return []

    image = cv2.imread(image_path)
    if image is None:
        print("Error loading image.")
        return []

    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_image)

    if not face_locations:
        print("No faces found in the image.")
        return []

    face_encodings = []
    for face_location in face_locations:
        encoding = face_recognition.face_encodings(rgb_image, [face_location])[0]
        face_encodings.append(encoding)

        top, right, bottom, left = face_location
        cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)

    cv2.imshow("Detected Faces", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return face_encodings
