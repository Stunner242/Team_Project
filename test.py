from flask import Flask, request, render_template
import cv2
import os
import time
from Check import check_credentials  # Importing the credential check function
from Studentcheck import check_Student
from StudentData import get_student_data
from Match import generate_face_encodings_from_image
from All_Student_data import get_all_student


# Create the Flask app
app = Flask(__name__)

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')  # This will look for index.html in the templates folder

# Route for the "Create Account" page
@app.route('/create-account')
def create_account():
    return render_template('index2.html')  # This will render index2.html page
# Route for teacher registrationcls
@app.route('/register-teacher')
def register_teacher():
    return render_template('Teacher.html') 

# Route for student registration
@app.route('/register-student')
def register_student():
    return render_template('Student.html')  #  This will render the Student.html 
@app.route('/take-attendance')
def take_attendance():
    return capture_images()  # Call the capture_images function to start capturing images
@app.route('/show-student-data')
def show_student():
    student_data = get_all_student()  # Get all student data from the database
    return render_template('show_student.html',students=student_data)  # This will render the show_student.html page 

# Route to handle form submission
@app.route('/start', methods=['POST'])
def start():
    username = request.form['first']
    password = request.form['password']
    role = request.form['role']

    # Check credentials in the database using the imported function
    if role == 'teacher':
        if check_credentials(username, password):
            return render_template('TeacherDashBoard.html',username=username)  # Call the webcam capture function if valid
        else:
            return "Invalid username or password."  # Return message if credentials are incorrect
    else:
        if role == 'student':
            if check_Student(username, password):
                student_data = get_student_data(username, password)
                if student_data:
                    return render_template('record.html', student=student_data)
                else:
                    return "Student data not found."
        else:
            return "Invalid username or password."
    return "Invalid username or password."
# Function to capture images
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

if __name__ == '__main__':
    app.run(debug=True)
