Face Detector (Haar Cascading)
A simple real-time face detection project using Python, OpenCV, and a Haar Cascade classifier.
This script detects faces from your webcam feed and draws a rectangle around them using a pre-trained Haar cascade model.
📌 Features
Real-time face detection from webcam
Uses OpenCV’s Haar cascade classifier
Easy to run and extend
🚀 Demo
When you run the script, your webcam opens and you’ll see a live video where faces are detected with rectangular frames.
🧠 How It Works
This project uses a machine learning-based object detection approach called Haar Cascades.
Haar cascades are trained on lots of positive (face) and negative (non-face) images. The model detects patterns and can spot faces in new images or video frames.
The detection flow is typically:
Capture video frame from webcam
Convert frame to grayscale
Run the cascade classifier to find faces
Draw boxes around detected faces
📦 Requirements
Make sure you have Python 3.x installed.
Install the needed libraries:
pip install opencv-python numpy
📁 Project Structure
face_detector.haarcascading/
├── face.py
├── haarcascade_frontalface_default.xml
└── README.md




