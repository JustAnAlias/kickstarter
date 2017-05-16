import json
from os.path import join, dirname
from watson_developer_cloud import VisualRecognitionV3


def classifyFromUrl(url):
        visual_recognition = VisualRecognitionV3('2016-05-20', api_key='2f26c30ef3bd18e4310f163da0fdbe7a0d2a6649')
        print(json.dumps(visual_recognition.classify(images_url=url), indent=2))

def classifyFromPath(path):
        visual_recognition = VisualRecognitionV3('2016-05-20', api_key='2f26c30ef3bd18e4310f163da0fdbe7a0d2a6649')
        print(json.dumps(visual_recognition.classify(images_file=path), indent=2))


#classifyFromUrl('https://www.ibm.com/ibm/ginni/images/ginni_bio_780x981_v4_03162016.jpg')
classifyFromPath('./bears-vs-babies-a-card-game-1-base/bears-vs-babies-a-card-game-1-base0.jpg')
