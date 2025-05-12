# MRI Brain Tumor Segmentation

This project uses OpenCV to process MRI brain images and segment potential tumors using image processing techniques. The goal is to enhance the image quality, apply adaptive thresholding, remove noise, and extract contours to identify regions that could potentially correspond to tumors.

## Features

- **Image Loading**: Load grayscale MRI images for processing.
- **Noise Reduction**: Apply median blur to reduce noise.
- **Thresholding**: Use adaptive thresholding to enhance important features.
- **Morphological Operations**: Remove small noise using morphological opening.
- **Contour Detection**: Identify and filter contours to highlight potential tumor regions.
- **Visualization**: Display the original, thresholded, and segmented images.

## Requirements

To run this project, you need to have the following installed:

- Python 3.x
- OpenCV library (`cv2`)
- Numpy library (`numpy`)

You can install the required libraries using `pip`:

```bash
pip install opencv-python numpy
````

## Usage

1. **Prepare your MRI Image**: Place the MRI image (in grayscale) you want to process in the same directory as the script. The script currently expects the file to be named `brain.jpg`. You can adjust the filename in the code if necessary.

2. **Run the Script**: Once the image is prepared, simply run the Python script:

   ```bash
   python mri_tumor_segmentation.py
   ```

3. **Output**: The script will display the following images:

   * **Original MRI**: The original grayscale MRI image.
   * **Thresholded Image**: The image after applying adaptive thresholding.
   * **Segmented Tumor**: The image with detected contours of possible tumors highlighted in green.

## Code Explanation

1. **Image Loading**: The image is loaded as a grayscale image using OpenCV's `cv2.imread()` function.

2. **Noise Reduction**: A median blur is applied using `cv2.medianBlur()` to reduce noise.

3. **Adaptive Thresholding**: Adaptive thresholding (`cv2.adaptiveThreshold()`) is applied to convert the image into a binary format to highlight important features.

4. **Morphological Operations**: The image undergoes morphological opening (`cv2.morphologyEx()`) to remove small blobs of noise.

5. **Contour Detection**: The contours are found using `cv2.findContours()`, and areas smaller than a threshold are ignored.

6. **Drawing Contours**: The contours are drawn on the original image where the area is larger than a specified threshold.

## Example

Here is how the program works with an example image:

* **Original Image**:

![Image](https://github.com/user-attachments/assets/3673480c-1b83-4cf7-9b8b-fadeda8574b0)

* **Thresholded Image**:

  ![Image](https://github.com/user-attachments/assets/85866953-61fe-4f04-aabd-351745969dce)

* **Segmented Tumor**:

  ![Image](https://github.com/user-attachments/assets/db081d6c-97ff-4805-942c-a9b86e9a8285)

## Notes

* The threshold value for contour area (`500` in the code) can be adjusted based on the specific image or required sensitivity.
* This script assumes that the MRI image is in grayscale. If working with colored images, preprocessing steps will need to be modified.


## Acknowledgements

* This project uses OpenCV for image processing.
* Inspiration taken from common computer vision techniques for medical image analysis.

```
