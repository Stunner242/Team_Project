import mysql.connector
def get_all_student(class_name):
    try:
        # Connect to the database
        conn = mysql.connector.connect(host='localhost', user='root', password='Golu123', database='garvit')
        cursor = conn.cursor()
        select_query = "SELECT id,username,gender,class,present,absent FROM student where class = %s"
        cursor.execute(select_query,(class_name,))
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
                'absent': student[5]
            })
        return student_data
    except mysql.connector.Error as err:
        print("Error:", err)
        return None