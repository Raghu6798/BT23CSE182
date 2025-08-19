import cv2
import numpy as np


image_path = r"C:\Users\Raghu\Downloads\Incidence_response_agent\DIP_LAB_2_BT23CSE182\assets\watermarked_images.jpg"
img = cv2.imread(image_path)

if img is None:
    print(f"Error: Could not load image from path: {image_path}")
    print("Please make sure the image is saved as 'watermarked_image.jpg' in the same directory as the script.")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    threshold_value = 215
    _, mask = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

    dst = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)

    output_path = "watermark_removed.jpg"
    cv2.imwrite(output_path, dst)

    print(f"Successfully removed watermark!")
    print(f"The clean image has been saved as: {output_path}") 
