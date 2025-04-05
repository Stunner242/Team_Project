import mysql.connector

def get_student_data(uname, passw, id1):
    uname = uname.strip()
    passw = passw.strip()
    id1 = id1.strip()

    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Golu123',
            database='garvit'
        )
        cursor = conn.cursor()

        # Step 1: Get student info
        select_student = "SELECT * FROM student WHERE username = %s AND password = %s AND id = %s"
        cursor.execute(select_student, (uname, passw, id1))
        student_result = cursor.fetchone()

        if not student_result:
            return None

        student_data = { 
            'id': student_result[0],
            'username': student_result[1],
            'password': student_result[2],
            'gender': student_result[3],
            'class': student_result[4],
            'roll_no': student_result[5],
        } # Extract student data

        # Step 2: Get all subject-wise attendance for the student
        select_attendance = "SELECT subject_name, present, absent FROM subject WHERE id = %s"
        cursor.execute(select_attendance, (student_data['id'],)) # Get attendance for the student
        attendance_results = cursor.fetchall()

        # Store attendance per subject
        attendance_list = []
        for subject_name, present, absent in attendance_results:
            attendance_list.append({
                'subject_name': subject_name,
                'present': present,
                'absent': absent
            })

        student_data['attendance'] = attendance_list ## Add attendance data to student_data
        return student_data

    except mysql.connector.Error as err:
        print("Error:", err)
        return None

    finally:
        cursor.close()
        conn.close()
