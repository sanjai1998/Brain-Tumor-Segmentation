import cv2
import numpy as np

# Load the MRI image (grayscale)
image = cv2.imread('C:\Users\anna_students\Desktop\Brain Tumor Segmentation\brain.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# Apply binary thresholding (you can tune the value)
_, thresh = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)

# Perform morphological operations to remove small noise
kernel = np.ones((5, 5), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# Find contours which may correspond to tumor
contours, _ = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on the original image
result = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.drawContours(result, contours, -1, (0, 255, 0), 2)

# Show images
cv2.imshow('Original', image)
cv2.imshow('Threshold', thresh)
cv2.imshow('Segmented Tumor', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
