import cv2
import numpy as np

def apply_canny_edge_detection(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply GaussianBlur to reduce noise and improve edge detection
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Apply Canny edge detection
    edges = cv2.Canny(blurred, 50, 150)
    
    return edges

def main():
    # Load an image from file
    image_path = "path/to/your/image.jpg"  # Replace with the path to your image
    original_image = cv2.imread(image_path)

    if original_image is None:
        print("Error: Could not read the image.")
        return

    # Apply Canny edge detection
    edges = apply_canny_edge_detection(original_image)

    # Display the original and the filtered images
    cv2.imshow('Original Image', original_image)
    cv2.imshow('Canny Edge Detection', edges)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
