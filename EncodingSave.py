import mysql.connector
import numpy as np
import base64
import zlib  # Compression library

def saveEncoding(encoding, name,roll_no,id):
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='Golu123', database='garvit')
        cursor = conn.cursor()

        # Convert NumPy array to bytes
        encoding_array = np.array(encoding, dtype=np.float32)
        encoding_bytes = encoding_array.tobytes()

        # Compress the encoding
        compressed_encoding = zlib.compress(encoding_bytes)

        # Convert to base64 for safe storage
        encoding_base64 = base64.b64encode(compressed_encoding).decode('utf-8')

        insert_query = "INSERT INTO face_encodings (id,name,roll_no, encoding) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (id,name,roll_no, encoding_base64))

        conn.commit()
        cursor.close()
        conn.close()
        return True
    except mysql.connector.Error as err:
        print("Error: ", err)
        return False
