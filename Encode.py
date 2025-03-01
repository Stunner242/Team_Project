import face_recognition
import cv2
from EncodingSave import saveEncoding

def generate_face_encodings_from_image(image_path):
    """Generates face encodings for all faces in an image and displays detected faces."""

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

    # Encode each detected face and draw a rectangle
    face_encodings = []
    for face_location in face_locations:
        encoding = face_recognition.face_encodings(rgb_image, [face_location])[0]
        face_encodings.append(encoding)

        # Draw a rectangle around the detected face
        top, right, bottom, left = face_location
        cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)

    # Show the image with detected faces
    cv2.imshow("Detected Faces", image)
    cv2.waitKey(0)  # Wait for a key press
    cv2.destroyAllWindows()  # Close the window

    return face_encodings

# Example usage
image_path = "s3.jpg"  # Path to the image
name = "Garvit"
roll_no = "21ESKIT303"
id = "B210964"

encodings = generate_face_encodings_from_image(image_path)
if encodings:
    saveEncoding(encodings, name, roll_no, id)
    print("Encoding saved successfully.")
else:
    print("No face encodings found.")
