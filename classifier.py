import json
#from os.path import join, dirname
import os
from watson_developer_cloud import VisualRecognitionV3


classifications = []
def classifyFromUrl(url):
         visual_recognition = VisualRecognitionV3('2016-05-20', api_key='2f26c30ef3bd18e4310f163da0fdbe7a0d2a6649')
         print(json.dumps(visual_recognition.classify(images_url=url), indent=2))

def classifyFromPath(path):
         visual_recognition = VisualRecognitionV3('2016-05-20', api_key='2f26c30ef3bd18e4310f163da0fdbe7a0d2a6649')
         return(visual_recognition.classify(images_file=open(path, 'rb')))


# with open('imageClassifications.json','w') as fp:
#     json.dump(classifyFromPath("videos/bring-reading-rainbow-back-for-every-child-everywh/frames/bring-reading-rainbow-back-for-every-child-everywh-1-base0.jpg"), fp, indent=4)

def allVideos(root_dir):
        for directory, subdirectories, files in os.walk(root_dir):
                for file in files:
                        file2json = file[:-4] + ".json"
                        with open(directory+file2json,'a') as fp:
                                #print(directory)
                                #print(path2frame)
                                #classifications.append(classifyFromPath(path2frame))
                                json.dump(classifyFromPath(os.path.join(directory, file)), fp, indent=4)
        

#print(classifications)
