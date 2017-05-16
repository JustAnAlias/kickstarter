import json
from os.path import join, dirname
from watson_developer_cloud import VisualRecognitionV3

test_url = 'https://www.ibm.com/ibm/ginni/images' \
           '/ginni_bio_780x981_v4_03162016.jpg'

visual_recognition = VisualRecognitionV3('2017-05-16', api_key='1UUq8kmpXJyD_n4Kn_CaQP0-tSQg1zvnNI1eVUlnDBSa')


print(json.dumps(visual_recognition.classify(images_url=test_url), indent=2))
