import face_recognition
import cv2
from CheckEncoding import check_Encoding
from updatepresent import update_present

def generate_face_encodings_from_image(image_path, class_name, subject_name):
    """Generates face encodings for all faces in an image."""

    image = cv2.imread(image_path)
    if image is None:
        print("Error loading image.")
        return []

    print(f"Image shape: {image.shape}, dtype: {image.dtype}")

    try:
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    except Exception as e:
        print(f"Error converting image to RGB: {e}")
        return []

    face_locations = face_recognition.face_locations(rgb_image)
    if not face_locations:
        print("No faces found in the image.")
        return []

    face_encodings = face_recognition.face_encodings(rgb_image, face_locations)

    any_matched = False
    for encoding in face_encodings:
        list1 = check_Encoding(encoding)
        if list1:
            stored_id = list1[0]
            stored_name = list1[1]
            if update_present(stored_id, class_name, subject_name):
                print("✅ Attendance marked for", stored_name, stored_id, subject_name)
            else:
                print("❌ Error marking attendance.")
            any_matched = True

    if not any_matched:
        
        print("😕 No match found for any face.")