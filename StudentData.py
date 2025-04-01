import mysql.connector


def get_student_data(uname,passw,id1):
    uname = uname.strip()
    passw = passw.strip()
    id1 = id1.strip()
    """
    Fetches the student data from the database based on the provided username.
    Returns the student data as a dictionary or tuple.
    """
    try:
        # Connect to the database
        conn = mysql.connector.connect(host='localhost', user='root', password='Golu123', database='garvit')
        cursor = conn.cursor()

        # Query to fetch student details based on username
        select_query = "SELECT * FROM student WHERE username = %s AND password = %s AND id = %s"
        cursor.execute(select_query, (uname,passw,id1))

        # Fetch the result of the query
        result = cursor.fetchone()  # Fetch only one record (first match)

        # Close the connection
        conn.close()

        # Check if the result is not None (student found)
        if result:
            # Return the data (could return a dictionary or tuple)
            student_data = {
                'id': result[0],  # Assuming the columns are: id, username, password, name, etc.
                'username': result[1],
                'password': result[2],
                'gender': result[3],
                'class': result[4], 
                'present' : result[5],
                'absent' : result[6],
            }
            return student_data
        else:
            return None  # If no student found with the given username

    except mysql.connector.Error as err:
        print("Error:", err)
        return None  # Return None in case of an error
