import mysql.connector

def update_present(roll_no, id):
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='Golu123', database='garvit')
        cursor = conn.cursor()

        # Fetch the current present count
        select_query = "SELECT present FROM Student WHERE roll_no = %s AND id = %s"
        cursor.execute(select_query, (roll_no, id))
        result = cursor.fetchone()

        # If present is NULL, set it to 0
        curr_present = result[0] if result and result[0] is not None else 0
        new_present = curr_present + 1

        # Update the present count
        update_query = "UPDATE Student SET present = %s WHERE roll_no = %s AND id = %s"
        cursor.execute(update_query, (new_present, roll_no, id))
        conn.commit()

        if cursor.rowcount == 1:
            return True

    except mysql.connector.Error as err:
        print("Error:", err)
        return None

    finally:
        cursor.close()
        conn.close()
