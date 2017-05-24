# USAGE
# python facial_landmarks.py --shape-predictor shape_predictor_68_face_landmarks.dat --image images/example_01.jpg

# import the necessary packages
from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2
import math

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True,
	help="path to facial landmark predictor")
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])

# load the input image, resize it, and convert it to grayscale
image = cv2.imread(args["image"])
image = imutils.resize(image, width=500)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect faces in the grayscale image
rects = detector(gray, 1)

def calc_distance(p1, p2):
	a = p1[0] - p2[0]
	b = p1[1] - p2[1]
	return math.sqrt(a*a + b*b)


# loop over the face detections
for (i, rect) in enumerate(rects):
	# determine the facial landmarks for the face region, then
	# convert the facial landmark (x, y)-coordinates to a NumPy
	# array
	shape = predictor(gray, rect)
	shape = face_utils.shape_to_np(shape)

	# convert dlib's rectangle to a OpenCV-style bounding box
	# [i.e., (x, y, w, h)], then draw the face bounding box
	(x, y, w, h) = face_utils.rect_to_bb(rect)
	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

	# show the face number
	cv2.putText(image, "Face #{}".format(i + 1), (x - 10, y - 10),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

	# loop over the (x, y)-coordinates for the facial landmarks
	# and draw them on the image
	shape_counter = 0
	points_list = []
	for (x, y) in shape:
		shape_counter += 1
		points_list.append((x,y))
		cv2.circle(image, (x, y), 1, (0, 0, 255), -1)
	point_counter = 0
	# for point in points_list:
	# 	point_counter += 1
	# 	print("point ", point_counter, " : ", point)

	# print("length of nose: ", np.linalg.norm(np.array(shape[28]), np.array(shape[31])))
# show the output image with the face detections + facial landmarks
nose_height = calc_distance(shape[28], shape[31])
nose_width = calc_distance(shape[32], shape[36])
eye_width = calc_distance(shape[37], shape[46])
face_height = math.fabs(shape[11][1] - shape[27][1]) + math.fabs(shape[7][1] - shape[18][1])
print("face height: ", face_height)
print("relation nose_height / nose_width: {0}\n relation nose_height / eye_width: {1}".format(nose_height/nose_width, nose_height/eye_width))

test1 = 0.7080854761617742/0.5574312636854032
test2 = 0.672428802050567/0.5025795528038837
print("ratio difference: ", test1/test2*100)


crap = 0
for i in range(68):
	crap += 68-i
print("total crap: ", crap)

cv2.imwrite(args["image"][:-4]+"marked"+args["image"][-4:], image)
cv2.imshow("Output", image)
cv2.waitKey(0)
