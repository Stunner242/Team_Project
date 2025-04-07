import mysql.connector
def get_all_student(class_name,subject_name):
    try:
        # Connect to the database
        conn = mysql.connector.connect(host='localhost', user='root', password='Golu123', database='garvit')
        cursor = conn.cursor()
        select_query =  """SELECT student.id, student.username, student.gender, student.class,subject.present, subject.absent,subject.subject_name
        FROM student
        JOIN subject ON student.id = subject.id AND student.class = subject.class
        WHERE subject.class = %s AND subject.subject_name = %s"""
        cursor.execute(select_query,(class_name,subject_name))
        result = cursor.fetchall()
        conn.close()
        student_data = []
        for student in result:
            student_data.append({
                'id': student[0],
                'username': student[1],
                'gender': student[2],
                'class': student[3],
                'present': student[4],
                'absent': student[5],
                'subject_name': student[6]
            })
        return student_data
    except mysql.connector.Error as err:
        print("Error:", err)
        return None