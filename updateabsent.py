import mysql.connector

def update_absent(present_ids, class_name, subject_name):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Golu123',
            database='garvit'
        )
        cursor = conn.cursor()

        # If some students are present, mark others absent
        if present_ids:
            format_strings = ','.join(['%s'] * len(present_ids))
            query = f"""
                UPDATE subject 
                SET absent = IFNULL(absent, 0) + 1 
                WHERE class = %s AND subject_name = %s 
                AND id NOT IN ({format_strings})
            """
            cursor.execute(query, (class_name, subject_name, *present_ids))
        else:
            # If no one is present, mark everyone as absent
            query = """
                UPDATE subject 
                SET absent = IFNULL(absent, 0) + 1 
                WHERE class = %s AND subject_name = %s
            """
            cursor.execute(query, (class_name, subject_name))

        conn.commit()
        print("✅ Absent updated successfully.")
    except Exception as e:
        print("❌ Error updating absent:", e)
    finally:
        cursor.close()
        conn.close()
