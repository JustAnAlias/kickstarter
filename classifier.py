import cv2
import json
from watson_developer_cloud import VisualRecognitionV3


test_url = 'https://www.ibm.com/ibm/ginni/images/ginni_bio_780x981_v4_03162016.jpg'

visual_recognition = VisualRecognitionV3('2016-05-20', api_key'1UUq8kmpXJyD_n4Kn_CaQP0-tSQg1zvnNI1eVUlnDBSa')


print(json.dumps(visual_recognition.classify(images_url=test_url), indent=2))

#cap = cv2.VideoCapture('/home/joni/Desktop/Python/kickstarter\video-768729-h264_base.mp4')  

#w, h = (640, 360)
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)
