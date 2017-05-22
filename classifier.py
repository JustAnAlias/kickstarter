import json
from os.path import join, dirname
from watson_developer_cloud import VisualRecognitionV3



def classifyFromUrl(url):
        visual_recognition = VisualRecognitionV3('2016-05-20', api_key='2f26c30ef3bd18e4310f163da0fdbe7a0d2a6649')
        print(json.dumps(visual_recognition.classify(images_url=url), indent=2))

def classifyFromPath(path):
        visual_recognition = VisualRecognitionV3('2016-05-20', api_key='2f26c30ef3bd18e4310f163da0fdbe7a0d2a6649')
        return(visual_recognition.classify(images_file=open(path, 'rb')))


with open('imageClassifications.json','w') as fp:
    json.dump(classifyFromPath("images.zip"), fp, indent=4)
