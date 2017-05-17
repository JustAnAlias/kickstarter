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

# local modules
from video import create_capture
from common import clock, draw_str


def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30),
                                     flags=cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

# bears-vs-babies-a-card-game-1-base.mp4

def run(folder, file_name):
    video_src = os.path.join(os.curdir, folder, file_name)
    images_folder = os.path.join(folder, 'frames')
    if not os.path.isdir(images_folder):
        os.mkdir(images_folder)
    if os.path.isfile(video_src):
        print('it is a file: ', video_src)
    else:
        print('no file you n00b', video_src)
    # args, video_src = getopt.getopt(sys.argv[1:], '', ['cascade=', 'nested-cascade='])
    # try:
    #     video_src = video_src[0]
    # except:
    #     video_src = 0
    # args = dict(args)
    # cascade_fn = args.get('--cascade', "haarcascade_frontalface_alt.xml")
    cascade_fn = "haarcascade_frontalface_alt.xml"
    # nested_fn  = args.get('--nested-cascade', "haarcascade_eye.xml")
    nested_fn  = "haarcascade_eye.xml"

    cascade = cv2.CascadeClassifier(cascade_fn)
    nested = cv2.CascadeClassifier(nested_fn)

    # cam = create_capture(video_src, fallback='synth:bg=../data/lena.jpg:noise=0.05')
    cam = cv2.VideoCapture(video_src)
    image_count = 0
    frame_count = 0
    while True:
        if frame_count % 500 == 0:
            print('faces found: ', image_count)
        ret, img = cam.read()
        if not ret:
            break
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        t = clock()
        rects = detect(gray, cascade)
        vis = img.copy()
        draw_rects(vis, rects, (0, 255, 0))
        if not nested.empty():
            for x1, y1, x2, y2 in rects:
                roi = gray[y1:y2, x1:x2]
                vis_roi = vis[y1:y2, x1:x2]
                subrects = detect(roi.copy(), nested)
                if len(subrects)>0:
                    save_file_to = os.path.join(images_folder, "{0}{1}.jpg".format(file_name[:-4], image_count))
                    # print('saving file to: ', save_file_to)
                    cv2.imwrite(save_file_to, img)
                    image_count += 1
                # draw_rects(vis_roi, subrects, (255, 0, 0))
        dt = clock() - t
        frame_count += 1

        # draw_str(vis, (20, 20), 'time: %.1f ms' % (dt*1000))
        #cv2.imshow('facedetect', vis)

        if cv2.waitKey(5) == 27:
            break
    print("{0} images made out of {1} frames".format(image_count, frame_count))
    cv2.destroyAllWindows()
if __name__ == '__main__':
    import sys, getopt
    print(__doc__)
    run("videos/bring-reading-rainbow-back-for-every-child-everywh", "bring-reading-rainbow-back-for-every-child-everywh-1-base.mp4")
