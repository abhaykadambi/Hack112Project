import cv2
import numpy as np

def detect_face(image):
    # Load OpenCV's pre-trained face detection model
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Convert image to grayscale (required by face detector)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # If at least one face is detected, crop the first face found
    if len(faces) > 0:
        (x, y, w, h) = faces[0]  # Coordinates of the first detected face
        face_image = image[y:y+h, x:x+w]  # Crop the face from the image
        return face_image
    else:
        return None  # If no face is detected, return None

def detect_skin(image):
    # Convert image to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Define lower and upper bounds for skin color in HSV
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)
    
    # Create a binary mask where white represents skin colors
    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    
    # Apply the mask to the original image
    skin = cv2.bitwise_and(image, image, mask=mask)
    
    return skin

def average_skin_color(images):
    skin_colors = []
    
    for image in images:
        # Detect and crop the face from the image
        face_image = detect_face(image)
        
        if face_image is not None:
            skin = detect_skin(face_image)
            
            # Reshape the skin image to a list of pixels
            pixels = skin.reshape(-1, 3)
            
            pixels = pixels[np.any(pixels != [0, 0, 0], axis=1)]
            
            if len(pixels) > 0:
                mean_color = np.mean(pixels, axis=0)
                skin_colors.append(mean_color)
    
    if len(skin_colors) > 0:
        average_color = np.mean(skin_colors, axis=0)
        return tuple(map(int, average_color))
    else:
        return None

def load_images(filepaths):
    images = []
    for filepath in filepaths:
        image = cv2.imread(filepath)
        if image is not None:
            images.append(image)
    return images

def display_color(color):
    color_image = np.zeros((100, 100, 3), np.uint8)
    color_image[:] = color

    cv2.imshow('Average Skin Color', color_image)

    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

def classify_fitzpatrick(rgb):
    r, g, b = rgb
    y = 0.299*r + 0.587*g + 0.114*b

    if y <= 80:
        return 6
    elif y <= 110:
        return 5
    elif y <= 150:
        return 4
    elif y <= 190:
        return 3
    elif y <= 230:
        return 2
    else:
        return 1

# Example usage
filepaths = ["IMG_8750.JPG"]

images = load_images(filepaths)
average_color = average_skin_color(images)

if average_color is not None:
    print("Average skin color (RGB):", average_color)

    fitzpatrick_type = classify_fitzpatrick(average_color)
    print("Fitzpatrick scale type:", fitzpatrick_type)
else:
    print("No face detected in the images.")
