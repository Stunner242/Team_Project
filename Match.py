import face_recognition
import cv2
from CheckEncoding import check_Encoding
from updatepresent import update_present

def generate_face_encodings_from_image(image_path,class_name,subject_name):
    """Generates face encodings for all faces in an image."""

    # Read the image using OpenCV
    image = cv2.imread(image_path)

    if image is None:
        
        print("Error loading image.")
        return []

    print(f"Image shape: {image.shape}, dtype: {image.dtype}")

    # Convert image to RGB (required by face_recognition)
    try:
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    except Exception as e:
        print(f"Error converting image to RGB: {e}")
        return []

    # Detect faces in the image
    face_locations = face_recognition.face_locations(rgb_image)

    if not face_locations:
        print("No faces found in the image.")
        return []

    # Encode each detected face
    face_encodings = []
    for face_location in face_locations:
        encoding = face_recognition.face_encodings(rgb_image, [face_location])[0]
        face_encodings.append(encoding)
    if face_encodings:
        list1=[]
        list1=check_Encoding(face_encodings[0])
        if list1:
            stored_id = list1[0]
            stored_name=list1[1]
            if update_present(stored_id,class_name,subject_name):
                print("Attendance marked for",stored_name,stored_id,subject_name)
            else:
                print("Error marking attendance.")

        else:
            print("No face encodings found.")
    else:
        print("No face encodings found.")


