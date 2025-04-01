import mysql.connector
def check_credentials(uname, passw,id1):
    uname = uname.strip()
    passw = passw.strip()
    id1 = id1.strip()
    try:
        # Establish connection to MySQL
        conn = mysql.connector.connect(host='localhost', user='root', password='Golu123', database='garvit')
        cursor = conn.cursor()

        # Query to check if the username and password exist
        select_query = "SELECT * FROM teacher WHERE username = %s AND password = %s AND id=%s"
        cursor.execute(select_query, (uname, passw,id1))

        # Fetch the result of the query
        result = cursor.fetchall()

        # Close the connection
        conn.close()

        # Return True if a match is found, otherwise False
        return len(result) > 0

    except mysql.connector.Error as err:
        print("Error: ", err)
        return False
