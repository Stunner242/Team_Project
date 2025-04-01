from flask import Flask, request, render_template
import cv2
import os
import time
from Check import check_credentials  # Importing the credential check function
from Studentcheck import check_Student
from StudentData import get_student_data
from All_Student_data import get_all_student
from TakeAttdence import capture_images



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
    return  capture_images()# Call the capture_images function to start capturing images
@app.route('/show-student-data')
def show_student():
    student_data = get_all_student()  # Get all student data from the database
    return render_template('show_student.html',students=student_data)  # This will render the show_student.html page 

# Route to handle form submission
@app.route('/start', methods=['POST'])
def start():
    username = request.form['first'].strip()
    password = request.form['password'].strip()
    id1=request.form['id'].strip()
    role = request.form['role'].strip()

    # Check credentials in the database using the imported function
    if role == 'teacher':
        if check_credentials(username, password,id1):
            return render_template('TeacherDashBoard.html',username=username)  # Call the webcam capture function if valid
        else:
            return "Invalid username or password."  # Return message if credentials are incorrect
    else:
        if role == 'student':
            if check_Student(username, password,id1):
                student_data = get_student_data(username, password,id1)  # Get student data from the database
                if student_data:
                    return render_template('record.html', student=student_data)
                else:
                    return "Student data not found."
        else:
            return "Invalid Student username or password."
    return "Invalid username or password."
if __name__ == '__main__':
    app.run(debug=True)
