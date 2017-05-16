import json
from os.path import join, dirname
from watson_developer_cloud import VisualRecognitionV3

test_url = 'https://www.ibm.com/ibm/ginni/images' \
           '/ginni_bio_780x981_v4_03162016.jpg'


#  2f26c30ef3bd18e4310f163da0fdbe7a0d2a6649

# visual_recognition = VisualRecognitionV3('2017-05-16', api_key='1UUq8kmpXJyD_n4Kn_CaQP0-tSQg1zvnNI1eVUlnDBSa')
#>>>>>>> 35894482d2af0e4b1d97666b06a77e97a9065820

# visual_recognition = VisualRecognitionV3('2017-05-16', api_key='1UUq8kmpXJyD_n4Kn_CaQP0-tSQg1zvnNI1eVUlnDBSa')
visual_recognition = VisualRecognitionV3('2017-05-16', api_key='2f26c30ef3bd18e4310f163da0fdbe7a0d2a6649')

print(json.dumps(visual_recognition.classify(images_url=test_url), indent=2))
