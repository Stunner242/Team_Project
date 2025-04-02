import mysql.connector
def get_teacher_data(username,id1):
    try:
        conn =  mysql.connector.connect(host='localhost', user='root', password='Golu123', database='garvit')
        cursor = conn.cursor()
        select_query="SELECT class FROM teacher where username=%s AND id=%s"
        cursor.execute(select_query,(username,id1))
        result = cursor.fetchall()
        conn.close()
        teacher=[]
        if result:
          
          for row in result:
            teacher.append(row[0])
        else:
            return "No Data Found"
        return teacher
        
    except mysql.connector.Error as err:
            print("Error:", err)
            return None