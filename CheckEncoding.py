import mysql.connector
import numpy as np
import base64
import zlib
import face_recognition  # Required for face comparison

def check_Encoding(encoding):
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='Golu123', database='garvit')
        cursor = conn.cursor()

        # Fetch all encodings from the database
        select_query = "SELECT id, name, roll_no, encoding FROM face_encodings"
        cursor.execute(select_query)
        results = cursor.fetchall()

        if not results:
            print("⚠️ No encodings found in the database.")
            return False

        print(f"🔍 Trying to match against {len(results)} stored encodings...")

        # Minimum distance found
        best_match = None
        best_distance = 1.0

        for row in results:
            stored_id = row[0]
            stored_name = row[1]
            stored_roll_no = row[2]
            stored_encoding_base64 = row[3]

            # Decode and decompress the stored encoding
            try:
                stored_encoding_bytes = base64.b64decode(stored_encoding_base64)
                stored_encoding_array = np.frombuffer(zlib.decompress(stored_encoding_bytes), dtype=np.float32)
            except Exception as e:
                print(f"⚠️ Error decoding encoding for {stored_name} ({stored_id}): {e}")
                continue

            # Calculate face distance
            distance = face_recognition.face_distance([stored_encoding_array], encoding)[0]
            print(f"🧠 Distance to {stored_name} ({stored_id}): {distance:.4f}")

            # Use strict tolerance threshold
            if distance < 0.45:
                if distance < best_distance:
                    best_distance = distance
                    best_match = [stored_id, stored_name, stored_roll_no]

        if best_match:
            print(f"✅ Match found: {best_match[1]} ({best_match[0]}) | Distance: {best_distance:.4f}")
            return best_match
        else:
            print("❌ No suitable match found.")
            return False

    except mysql.connector.Error as err:
        print("❌ Database error:", err)
        return False

    finally:
        cursor.close()
        conn.close()
