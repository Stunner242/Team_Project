import face_recognition
import cv2
from CheckEncoding import check_Encoding
from updatepresent import update_present


def generate_face_encodings_from_image(image_path, class_name, subject_name):
    """Generates face encodings for all faces in an image."""

    image = cv2.imread(image_path)
    if image is None:
        print("Error loading image.")
        return [],[],None

    print(f"Image shape: {image.shape}, dtype: {image.dtype}")
    
    try:
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    except Exception as e:
        print(f"Error converting image to RGB: {e}")
        return [],[],None

    face_locations = face_recognition.face_locations(rgb_image)
    Blank = []
    if not face_locations:
        Blank.append("No faces found in the image.")
        return Blank,[],None

    face_encodings = face_recognition.face_encodings(rgb_image, face_locations)

    attendance_results = []
    present_id=[]
    for encoding in face_encodings:
        list1 = check_Encoding(encoding)
        if list1:
            stored_id = list1[0]
            stored_name = list1[1]
            if stored_id not in present_id:
                present_id.append(stored_id)
            if update_present(stored_id, class_name, subject_name):
                message = f" Attendance marked for {stored_name} ({stored_id})"
            else:
                message = f"Error marking attendance for {stored_name} ({stored_id})"
            attendance_results.append(message)

        

    if not attendance_results:
        attendance_results.append("No match with any face.")
    return attendance_results,present_id,stored_id