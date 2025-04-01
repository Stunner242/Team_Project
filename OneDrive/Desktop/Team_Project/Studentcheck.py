import mysql.connector

def check_Student(uname,passw,id1):
    uname = uname.strip()
    passw = passw.strip()
    id1 = id1.strip()
    """
    Checks if the given username and password exist in the database.
    Returns True if the credentials are valid, otherwise False.
    """
    try:
        # Establish connection to MySQL
        conn = mysql.connector.connect(host='localhost', user='root', password='Golu123', database='garvit')
        cursor = conn.cursor()
        print(f"Checking for Username: '{uname}', Password: '{passw}', ID: '{id1}'")

        # Query to check if the username and password exist
        select_query = "SELECT * FROM student WHERE username = %s AND password = %s AND id = %s"
        cursor.execute(select_query, (uname,passw,id1))

        # Fetch the result of the query
        result = cursor.fetchall()

        # Close the connection
        conn.close()

        # Return True if a match is found, otherwise False
        return len(result) > 0

    except mysql.connector.Error as err:
        print("Error: ", err)
        return False
