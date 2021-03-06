#!/usr/bin/env python

# Python 2/3 compatibility
from __future__ import print_function

import numpy as np
import cv2
import os
import dlib
import math

# local modules
from video import create_capture
from common import clock, draw_str


VEC_DIFF_LIMIT = 5

face_list = []
# bears-vs-babies-a-card-game-1-base.mp4

def have_face(face_id):
    face_differences = []
    for i in range(len(face_list)):
        diff_val = 0
        for j in range(len(face_id)):
            diff_val += math.fabs(face_id[j]-face_list[i][j])
            if diff_val >= VEC_DIFF_LIMIT:
                break
        if diff_val < VEC_DIFF_LIMIT:
            return True
    return False

    high_diff_list = []
    for i in diff_list:
        if i > 3.6:
            high_diff_list.append(i)
    print("highest differences : ", high_diff_list)
        # for idx in range(1, len(face_list)):

def process_video(folder, file_name=None):
    video_src = os.path.join(os.curdir, folder, file_name)
    images_folder = os.path.join(folder, 'frames')
    if not os.path.isdir(images_folder):
        os.mkdir(images_folder)
    if os.path.isfile(video_src):
        print('it is a file: ', video_src)
    else:
        print('no file you n00b', video_src)
    predictor_path = "shape_predictor_68_face_landmarks.dat"
    face_rec_model_path = "dlib_face_recognition_resnet_model_v1.dat"

    detector = dlib.get_frontal_face_detector()
    sp = dlib.shape_predictor(predictor_path)
    facerec = dlib.face_recognition_model_v1(face_rec_model_path)
    cam = cv2.VideoCapture(video_src)
    image_count = 0
    frame_count = 0
    while True:
        frame_count += 1
        if frame_count % 1000 == 1:
            print('frames processed: ', frame_count-1) # yes, it's off by one, but looks better with whole thousands
        ret, img = cam.read()
        if not ret:
            break
        if not int(cam.get(cv2.CAP_PROP_POS_FRAMES)) % 15 == 0:
            continue


        # Ask the detector to find the bounding boxes of each face. The 1 in the
        # second argument indicates that we should upsample the image 1 time. This
        # will make everything bigger and allow us to detect more faces.
        dets = detector(img, 1)
        # print("Number of faces detected: {}".format(len(dets)))
        if len(dets) > 0:

        # Now process each face we found.
            for k, d in enumerate(dets):
                # print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
                    # k, d.left(), d.top(), d.right(), d.bottom()))
                # Get the landmarks/parts for the face in box d.
                shape = sp(img, d)

                # Compute the 128D vector that describes the face in img identified by
                # shape.
                face_id = facerec.compute_face_descriptor(img, shape)
                if not have_face(face_id):
                    print("new face found at frame number {0}".format(frame_count))
                    face_list.append(facerec.compute_face_descriptor(img, shape))
                    save_file_to = os.path.join(images_folder, "{0}{1}.jpg".format(file_name[:-4], image_count))
                    # save image as file
                    cv2.imwrite(save_file_to, img)
                    image_count += 1


    print("{0} images made out of {1} frames".format(image_count, frame_count))
    cv2.destroyAllWindows()

def run():
    import sys, getopt, json
    print(__doc__)
    startdata = None
    with open("data.json", "r") as f:
        startdata = json.load(f)
    for k in startdata.keys():

        fo = os.path.join("videos", k)
        fi = "{0}{1}".format(k, "-1-base.mp4")
        process_video(fo, fi)
        # p = "videos/"+k
        # f = k+"-1-base.mp4"
        # print(p)
        # print(f)
        # run(p,f)

if __name__ == '__main__':
    run()


    # run("videos/bring-reading-rainbow-back-for-every-child-everywh", "bring-reading-rainbow-back-for-every-child-everywh-1-base.mp4")
