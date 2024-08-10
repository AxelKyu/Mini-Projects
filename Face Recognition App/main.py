import threading
import cv2
from deepface import DeepFace

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)       # Creating a capture device that records from the first camera

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 620)   # Camera prop window has a width of 620
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Camera prop window has a width of 480

counter = 0     # Creating this so the camera doesn't look for face verification every single time More over like a check system

face_match = False

reference_img = cv2.imread("")

while True:
    ret, frame = cap.read()

    if ret:
        pass

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()