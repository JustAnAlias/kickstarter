#import cv2
#print(cv2.__version__)
#vidcap = cv2.VideoCapture('video-768729-h264_base.mp4')
#success,image = vidcap.read()
#count = 0
#success = True
#while success:
#  success,image = vidcap.read()
#  print('Read a new frame: ', success)
#  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
#  count += 1

# create a folder to store extracted images
import os
folder = 'test'  
os.mkdir(folder)
# use opencv to do the job
import cv2
print(cv2.__version__)  # my version is 3.1.0
vidcap = cv2.VideoCapture('video-768729-h264_base.mp4')
count = 0
while True:
    success,image = vidcap.read()
    if not success:
        break
    cv2.imwrite(os.path.join(folder,"frame{:d}.jpg".format(count)), image)     # save frame as JPEG file
    count += 1
print("{} images are extacted in {}.".format(count,folder))
