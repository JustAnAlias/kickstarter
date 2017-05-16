import cv2

cap = cv2.VideoCapture('/home/joni/Desktop/Python/kickstarter\video-768729-h264_base.mp4')  

w, h = (640, 360)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)
