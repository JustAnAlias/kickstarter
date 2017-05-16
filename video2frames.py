import os
import cv2

def makeFrames(videofile):
        videoname = videofile[:-4]
        folder = videoname
        os.mkdir(folder)

        vidcap = cv2.VideoCapture(videofile)
        count = 0
        while True:
                success,image = vidcap.read()
                if not success:
                        break
                cv2.imwrite(os.path.join(folder,videoname+"{:d}.jpg".format(count)), image)
                count += 1
                if(count % 100 == 0):
                        print(count, "frames extracted")
        print("{} images are extracted in {}.".format(count,folder))

makeFrames('videovideo.mp4')
