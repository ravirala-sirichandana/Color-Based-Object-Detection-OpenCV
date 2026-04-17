# 🚀Color-Based Object Detection and Tracking using OpenCV

This project demonstrates **color-based object detection and tracking** using OpenCV in Python.  
By selecting a specific color range (in HSV color space), the system detects the object in the video frame and either:

- Tracks the **centroid** of the object and draws its path, or  
- Highlights the object with **colored dots** on the detected regions.

The project uses a webcam/video feed and simple computer vision techniques like color thresholding and contour detection.

# Project Structure
Color-Based-Object-Detection-OpenCV/
    -code
       - color_tracking_centroid.py   
       -color_detection_dots.py         

    -sample_outputs/
       -drawing_20250506_235351           
       -drawing_20250507_221242
       -drawing_20250506_234522

    - documentation/
       - Project_Presentation.pptx      
    -requirements.txt                    
    -README.md                           
    -LICENSE                             

# Key Concepts Used

-HSV Color Space for robust color detection
-Color thresholding using cv2.inRange()
-Morphological operations (optional) to clean noise
-Contours to find object boundaries
-Centroid calculation to track object position frame-by-frame
-Real-time video processing using webcam

# Installation

Clone the repository:
git clone https://github.com/ravirala-sirichandana/Color-Based-Object-Detection-OpenCV.git
cd Color-Based-Object-Detection-OpenCV
Create and activate a virtual environment (optional but recommended):
python -m venv venv
venv\Scripts\activate            # On Windows
# source venv/bin/activate       # On macOS / Linux

# Install dependencies:

pip install -r requirements.txt

# How to Run the Codes
1. Centroid-Based Color Tracking
File: code/color_tracking_centroid.py
This script:

-Captures video from the webcam
-Detects the specified color
-Finds the contour of the object
-Calculates the centroid
-Draws a trail/path showing the movement of the object

Run:
python code/color_tracking_centroid.py

Move the colored object (e.g., blue object) in front of your webcam.
You will see a bounding shape and a path showing how the object moves.

2. Color Detection with Dots
File: code/color_detection_dots.py
This script:

-Captures video from the webcam
-Detects all regions in the frame that match the selected color
-Marks them with small colored dots / circles

Run:
python code/color_detection_dots.py

All areas with that color will be highlighted with dots on the screen.

# Changing the Target Color

Both scripts use a color range in HSV format.
You can adjust the lower and upper HSV values in the code to detect different colors:

# Example (inside the Python code)
lower_hsv = np.array([H_min, S_min, V_min])
upper_hsv = np.array([H_max, S_max, V_max])
For blue, green, red, etc., you can experiment by changing these values.
You can also use a color range finder tool to get HSV ranges more accurately.

# Sample Outputs

Check the sample_outputs/ folder for some example screenshots:
-drawing_20250506_234522
-drawing_20250506_235351
-drawing_20250507_221242
-drawing_20250507_222033
-drawing_20250507_224719
These images show how the system detects and tracks colored objects.

# Documentation

The detailed explanation and slides of this project are available in:
documentation/Color-Based Object Detection and Tracking Using OpenCV.pptx

You can open it with PowerPoint / LibreOffice Impress to see:

-Problem statement
-Objectives
-Methodology
-System design & workflow
-Output screenshots
-Conclusion and future work

# Author

Name: Siri Chandana Ravirala
Department: Information Technology
