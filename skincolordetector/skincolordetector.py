import cv2
import numpy as np

def detect_skin(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)
    
    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    
    skin = cv2.bitwise_and(image, image, mask=mask)
    
    return skin

def average_skin_color(images):
    skin_colors = []
    
    for image in images:
        skin = detect_skin(image)
        
        pixels = skin.reshape(-1, 3)
        

        pixels = pixels[np.any(pixels != [0, 0, 0], axis=1)]
        
        if len(pixels) > 0:
            mean_color = np.mean(pixels, axis=0)
            skin_colors.append(mean_color)
    

    average_color = np.mean(skin_colors, axis=0)
    
    return tuple(map(int, average_color))

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
    cv2.waitKey(0)
    cv2.destroyAllWindows()

filepaths = ["image1.jpg", "image2.jpg", "image3.jpg", "image4.jpg", "image5.jpg"]
images = load_images(filepaths)
average_color = average_skin_color(images)
print("Average skin color (RGB):", average_color)

display_color(average_color)
