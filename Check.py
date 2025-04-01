import mysql.connector

<<<<<<< HEAD
def check_credentials(uname, passw,id1):
    uname = uname.strip()
    passw = passw.strip()
    id1 = id1.strip()
=======
def check_credentials(uname, passw):
>>>>>>> 12f04d5df851cc5dafc55c732e6b5c37374e39f7
    """
    Checks if the given username and password exist in the database.
    Returns True if the credentials are valid, otherwise False.
    """
    try:
        # Establish connection to MySQL
        conn = mysql.connector.connect(host='localhost', user='root', password='Golu123', database='garvit')
        cursor = conn.cursor()

        # Query to check if the username and password exist
<<<<<<< HEAD
        select_query = "SELECT * FROM teacher WHERE username = %s AND password = %s AND id=%s"
        cursor.execute(select_query, (uname, passw,id1))
=======
        select_query = "SELECT * FROM login WHERE username = %s AND password = %s"
        cursor.execute(select_query, (uname, passw))
>>>>>>> 12f04d5df851cc5dafc55c732e6b5c37374e39f7

        # Fetch the result of the query
        result = cursor.fetchall()

        # Close the connection
        conn.close()

        # Return True if a match is found, otherwise False
        return len(result) > 0

    except mysql.connector.Error as err:
        print("Error: ", err)
        return False
