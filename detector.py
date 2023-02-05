import cv2
import numpy as np

def detect_deepfakes(video):
    # Load the video using OpenCV
    cap = cv2.VideoCapture(video)

    # Initialize variables to store the previous frame
    prev_frame = None

    # Read the frames in the video
    while True:
        # Read the current frame
        ret, frame = cap.read()

        # Break the loop if the video has ended
        if not ret:
            break

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Calculate the absolute difference between the current and previous frames
        diff = cv2.absdiff(gray, prev_frame)

        # Store the current frame for use in the next iteration
        prev_frame = gray

        # Threshold the difference to eliminate noise
        _, diff = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

        # Calculate the number of white pixels in the difference image
        white_pixels = np.sum(diff == 255)

        # If the number of white pixels is above a certain threshold, the frame is deemed to contain tampering
        if white_pixels > 10000:
            print("Deepfake detected in frame")

    # Release the video capture
    cap.release()

# Example usage
video = "video.mp4"
detect_deepfakes(video)
