# Drowsiness Detection System

A real-time drowsiness detection system that uses computer vision to detect if a driver's eyes are closed for an extended period, triggering an alert sound to help prevent accidents due to drowsy driving.

## Features

- Real-time face and eye detection using Haar Cascade classifiers
- Alerts the driver with a beep sound when drowsiness is detected
- Simple and lightweight implementation using OpenCV and Pygame
- Visual feedback with face detection rectangle

## Prerequisites

- Python 3.x
- OpenCV (`pip install opencv-python`)
- Pygame (`pip install pygame`)
- Webcam

## Installation

1. Clone this repository or download the files
2. Ensure all required files are in the same directory:
   - `new1.py` (main script)
   - `haarcascade_frontalface_default.xml` (face detection model)
   - `haarcascade_eye.xml` (eye detection model)
   - `beepsound.mp3` (alert sound)

## Usage

1. Run the script:
   ```
   python new1.py
   ```
2. Position yourself in front of the webcam
3. The system will detect your face and monitor your eyes
4. If your eyes are closed for more than 7 seconds, an alert sound will play
5. Press ESC to exit the application

## How It Works

1. The system captures video from your webcam
2. It detects faces using Haar Cascade classifier
3. For each detected face, it looks for eyes
4. If no eyes are detected for more than 7 seconds, it triggers an alert
5. The alert stops when open eyes are detected again

## Note

- Ensure proper lighting for better detection
- The system works best when facing the camera directly
- The sensitivity can be adjusted by modifying the `sec` threshold in the code

## License

This project is open source and available under the MIT License.
