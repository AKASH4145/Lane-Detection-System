## Lane Detection System (Computer Vision)

A Computer Vision project that detects road lane markings from videos using classical image processing techniques. The system identifies lane boundaries and highlights the driving lane in realtime. Lane detection is an essential component in Autonomous Driving and Advanced Driver Assistance Systems (ADAS). This project implements a pipeline that processes road images and detects lane lines using edge detection and line detection techniques.

The detected lanes are visualized by:
   - Drawing left and right lane boundaries
   - Highlighting the drivable region between lanes

---

## Concepts Used
 This project uses classical Computer Vision techniques instead of deep learning.

 Main algorithms used:

   - Canny Edge Detection (detects edges in the road image)
   - Hough Transform (detects straight lines from edge images)

 Other techniques:

   - Region of Interest masking
   - Slope based lane classification
   - Line averaging for stable lanes
   - Polygon lane overlay visualization

---

## Processing Pipeline

 The lane detection pipeline follows these steps:
   - Frame Capture
   - Grayscale Conversion
   - Noise Reduction
   - Edge Detection
   - Region of Interest (ROI)
   - Line Detection
   - Lane Classification
   - Lane Averaging
   - Lane Visualization

---

##  Features

 - Real-time Lane Detection
 - Edge Detection Pipeline
 - Line Detection
 - Slope-Based Lane Classification
 - Lane Region Highlighting
 - Works with Images and Videos
 - Lightweight and Fast
 - Modular Pipeline 


---

##  Motivation

Lane detection is a key component of Autonomous Driving and Advanced Driver Assistance Systems (ADAS). It helps vehicles understand road boundaries and stay within lanes.

This project explores how classical computer vision techniques like Canny Edge Detection and Hough Transform can be used to detect lane markings from images and videos. The goal is to understand how visual data can be processed to extract meaningful road information using a simple computer vision pipeline


---

##  Tech Stack
- Language : Python  
- Libraries : OpenCV , numpy  

---

##  System Architecture

Workflow:
1. Frame Input 
2. Preprocessing
3. Edge Detection
4. Region of Interest (ROI)
5. Line Detection 
6. Lane Classification
7. Lane Averaging
8. Lane Visualization 

---

##  Project Structure

```text
LANE DETECTION/
├── detection.py
├── Sample videos/
│   └── dashcam.mp4
├── Demo Screenshots/
│    ├──Detected Lane.png
│    ├──Edge Detection.png
│    └──ROI.png
│    
└── README.md

```
---

## Setup & Run

- git clone https://github.com/AKASH4145/Lane-Detection-System
- cd   Lane-Detection-System  
- pip install -r requirements.txt  
- python detector.py

---

## Demo Screenshots and Video
 ![Detected Lane](Demo%20Screenshots/Detected%20Lane.png)
 ![Edge Detection](Demo%20Screenshots/Edge%20Detection.png)
 ![Region of interest (ROI)](Demo%20Screenshots/ROI.png)
 🎥 Demo Video:  https://drive.google.com/file/d/1O2Kr_UTPYjGhOym_6YZh43Ou8NtxsDsc/view?usp=sharing

---

## Observations

- Classical computer vision techniques can successfully detect lane lines in well-lit road conditions.

- Edge detection combined with line detection provides a fast and lightweight solution for lane detection.

- Slope filtering and lane averaging help reduce noise and produce more stable lane boundaries.

- The system works best when lane markings are clear and well-defined

---

## Limitations

- performance decreases when lane markings are faded, worn out, or partially occluded.

- The system struggles in low-light conditions, shadows, or heavy rain.

- Curved lanes may not be detected accurately since the algorithm assumes mostly straight lane lines.

- Detection accuracy depends heavily on camera angle and road conditions

---

## Future Scope

- Deep learning lane detection using CNNs
- Real-time webcam lane detection
- Curved lane detection
- Lane departure warning system
- Steering angle prediction

---

## Applications 

- Autonomous vehicles
- Driver assistance systems
- Self-driving research
- Smart transportation systems

## Author

Akash GS | Mechanical Engineering student exploring AI, computer vision, and applied Python development

---