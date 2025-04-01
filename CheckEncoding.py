import mysql.connector
import numpy as np
import base64
import zlib
import face_recognition  # Required for face comparison

def check_Encoding(encoding):
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='Golu123', database='garvit')
        cursor = conn.cursor()

        # Fetch all encodings for the given user
        select_query = "SELECT id,name,roll_no,encoding FROM face_encodings"
        cursor.execute(select_query)
        results = cursor.fetchall()

        if not results:
            print("No encoding found for this user.")
            return False

        for row in results:
            stored_id=row[0]
            stored_name=row[1]
            stored_roll_no=row[2]
            stored_encoding_base64 = row[3] # Extract stored encoding

            # Decode Base64
            stored_encoding_bytes = base64.b64decode(stored_encoding_base64)

            # Decompress using zlib
            stored_encoding_array = np.frombuffer(zlib.decompress(stored_encoding_bytes), dtype=np.float32)

            # Compare with face_recognition
            match = face_recognition.compare_faces([stored_encoding_array], encoding, tolerance=0.6)
            list1=[stored_id,stored_name,stored_roll_no] 

            if match[0]: # If match found
                return list1

        return False

    except mysql.connector.Error as err:
        print("Error:", err)
        return False

    finally:
        cursor.close()
        conn.close()
