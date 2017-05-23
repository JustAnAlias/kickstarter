#!/usr/bin/env python

'''
face detection using haar cascades

USAGE:
    facedetect.py [--cascade <cascade_fn>] [--nested-cascade <cascade_fn>] [<video_source>]
'''

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

def run(folder, file_name):
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



    # cam = create_capture(video_src, fallback='synth:bg=../data/lena.jpg:noise=0.05')
    cam = cv2.VideoCapture(video_src)
    image_count = 0
    frame_count = 0
    while True:
        frame_count += 1
        if frame_count % 100 == 1:
            print('frames processed: ', frame_count-1)

        ret, img = cam.read()
        if not int(cam.get(cv2.CAP_PROP_POS_FRAMES)) % 15 == 0:
            continue

        if not ret:
            break
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
                # Draw the face landmarks on the screen so we can see what face is currently being processed.
                # win.clear_overlay()
                # win.add_overlay(d)
                # win.add_overlay(shape)

                # Compute the 128D vector that describes the face in img identified by
                # shape.  In general, if two face descriptor vectors have a Euclidean
                # distance between them less than 0.6 then they are from the same
                # person, otherwise they are from different people.  He we just print
                # the vector to the screen.
                face_id = facerec.compute_face_descriptor(img, shape)
                if not have_face(face_id):
                    print("new face found at frame number {0}".format(frame_count))
                    face_list.append(facerec.compute_face_descriptor(img, shape))
                    save_file_to = os.path.join(images_folder, "{0}{1}.jpg".format(file_name[:-4], image_count))
                    # print('saving file to: ', save_file_to)
                    cv2.imwrite(save_file_to, img)
                    image_count += 1
        # draw_str(vis, (20, 20), 'time: %.1f ms' % (dt*1000))
        #cv2.imshow('facedetect', vis)

    print("{0} images made out of {1} frames".format(image_count, frame_count))
    cv2.destroyAllWindows()
if __name__ == '__main__':
    import sys, getopt, json
    print(__doc__)
    startdata = None
    with open("data.json", "r") as f:
        startdata = json.load(f)
    for k in startdata.keys():
        p = "videos/"+k
        f = k+"-1-base.mp4"
        print(p)
        print(f)
        run(p,f)

    # run("videos/bring-reading-rainbow-back-for-every-child-everywh", "bring-reading-rainbow-back-for-every-child-everywh-1-base.mp4")
