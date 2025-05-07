from flask import Flask, request, render_template, Response
from pymongo import MongoClient
import gridfs
from bson.objectid import ObjectId
from datetime import datetime
from Check import check_credentials
from Studentcheck import check_Student
from StudentData import get_student_data
from All_Student_data import get_all_student
from All_teacher_data import get_teacher_data
from TakeAttdence import capture_images
from Getimage import get_image
from Admin import check_Admin

import Encode  # <- import your updated encode.py

client = MongoClient("mongodb://localhost:27017")
db = client["Attendance"]
fs = gridfs.GridFS(db)

app = Flask(__name__)

def delete_old_files():
    today_date = datetime.now().strftime('%Y-%m-%d')
    old_files = db.fs.files.find({
        "metadata.date": {"$ne": today_date}  # Only NOT today’s images
    })
    for file in old_files:
        fs.delete(file["_id"])

# Call the function on app startup
delete_old_files()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Next_Student')
def next_student():
    return render_template('Student.html')

@app.route('/Stop_Server')
def stop_server():
    return "Server Stopped"

@app.route('/teacher-dashboard')
def teacher_dashboard():
    class_name = request.args.get('class_name')
    subject_name = request.args.get('subject_name')
    username = request.args.get('username')
    return render_template('TeacherDashBoard.html', class_name=class_name, subject_name=subject_name, username=username)

@app.route('/take_attendance')
def take_attendance():
    class_name = request.args.get('class_name')
    subject_name = request.args.get('subject_name')
    return capture_images(class_name, subject_name)

@app.route('/show_faces')
def show_faces():
    class_name = request.args.get('class_name')
    subject_name = request.args.get('subject_name')
    image_list = get_image(class_name, subject_name)
    return render_template('Show_faces.html', image_list=image_list)

@app.route('/image/<file_id>')
def serve_image(file_id):
    file = fs.get(ObjectId(file_id))
    return Response(file.read(), mimetype='image/jpeg')

@app.route('/show_student')
def show_student():
    class_name = request.args.get('class_name')
    subject_name = request.args.get('subject_name')
    student_data = get_all_student(class_name, subject_name)
    return render_template('show_student.html', students=student_data)

@app.route('/start', methods=['POST'])
def start():
    username = request.form['first'].strip()
    password = request.form['password'].strip()
    id1 = request.form['id'].strip()
    role = request.form['role'].strip()

    # Check if role is faculty
    if role == 'faculty':
        if check_credentials(username, password, id1):
            classes_data = get_teacher_data(username, id1)
            return render_template('Classes.html', classes=classes_data, username=username)
        else:
            return "Invalid Faculty Credentials."  # Return an error with a proper response

    # Check if role is student
    elif role == 'student':
        if check_Student(username, password, id1):
            student_data = get_student_data(username, password, id1)
            if student_data:
                return render_template('record.html', student=student_data)
        else:
            return "Invalid Student Credentials" # Return an error if student data not found

    # Check if role is admin
    elif role == 'admin':
        if check_Admin(username, password, id1):
            return render_template('Student.html')
        else:
            return "Invalid Admin Credentials." # Return a forbidden error if admin credentials are invalid

    # Return an error if the role is not recognized
    return "Invalid role specified.", 400  # Return a bad request error

@app.route('/student_capture', methods=['POST'])
def student_capture():
    return Encode.process_student_registration()

if __name__ == '__main__':
    app.run(debug=True)
