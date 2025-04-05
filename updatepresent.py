import mysql.connector

def update_present(id,class_name, subject_name):
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='Golu123', database='garvit')
        cursor = conn.cursor()

        # Fetch the current present count
        select_query = "SELECT present FROM subject WHERE class = %s AND subject_name = %s AND id = %s"
        cursor.execute(select_query, (class_name, subject_name, id))
        result = cursor.fetchone()

        # If present is NULL, set it to 0
        curr_present = result[0] if result and result[0] is not None else 0
        new_present = curr_present + 1

        # Update the present count
        update_query = "UPDATE subject SET present = %s WHERE subject_name = %s AND id = %s AND class = %s"
        cursor.execute(update_query, (new_present,subject_name, id, class_name))
        conn.commit()

        if cursor.rowcount == 1:
            return True

    except mysql.connector.Error as err:
        print("Error:", err)
        return None

    finally:
        cursor.close()
        conn.close()
