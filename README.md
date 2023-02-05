# realsense
Simple deepfake detector. 
This code reads the frames of a video and calculates the difference between each frame and the previous frame. The difference image is then thresholded to eliminate noise and the number of white pixels is calculated. If the number of white pixels is above a certain threshold, the frame is deemed to contain tampering, indicating the presence of a deepfake. This is one example method of detecting deepfakes using AI.
Uses `OpenCV` library
