import mysql.connector
def saveStudentData(id, name, passw1, gender, class1, roll_no, email, phone):
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='Golu123', database='garvit')
        cursor = conn.cursor()
        insert_query = """
            INSERT INTO student 
            (id, username, password, gender, class, Roll_no, email, phone) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (id, name, passw1, gender, class1, roll_no, email, phone))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except mysql.connector.Error as err:
        print("Error: ", err)
        return False
