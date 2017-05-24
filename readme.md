![alt tag](https://github.com/JustAnAlias/kickstarter/blob/master/pictures/kickstarter-logo.png)

# Description

This project can be used to collect, organize and analyze on data from kickstarter.com
### Gathering relevant information
kickstarter.py (retrieves the nessecary data for the relevant projects on kickstarter, and saves it in a json file "data.json")
### Downloading video files automatically
ks_video_downloader.py (this script will automatically download videos from all of the projects that is saved in the "data.json" file, to you local machine or in this case to the virtual python environment)
### Detect whether the videos contains face and splits the video into usable images

1. facedetect_2_proto.py (dlib) uses another python library than facedetect.py and is far better at recognizing and detecting faces in the videos. This script will recognize the persons already seen in the video and save a single images of each person. This script will iterate alot faster over each frame in the video and save alot fewer pictures- therefore it is more time efficient and less space is required on your harddrive. BUT if for some reason you can not run this script because of missing modules etc. then use facedetect.py

2. facedetect.py will (opencv) read the subdirectories of the directory "/videos" and look for any .mp4 files and view every single frame of the video as a picture and if it detects a face, it will save the picture- This is our first implementation (saves too many pictures) 

### Watson IBM Famous AI - This script will look at the frames we saved and tell us with a fairly high certainty what there is, in the picture.

classifier.py will go through the subdirectories in "/video" and suck them in, and spit out alot information about what it thinks is on the pictures - To have this running you are ought to have a valid API-Key (retrieved from www.bluemix.net - Costs money)
We use this script to fast and effectively collect data of the pictures without even looking at them, the data we collect can now be used for analysis.


## Lets get started

### Prerequisites
1. git - 
2. Virtualbox - https://www.virtualbox.org/wiki/Downloads
3. Vagrant - https://www.vagrantup.com/downloads.html
4. SSH-Client
 - Windows - We recommend http://www.putty.org/
 - ubuntu  - SSH is already installed in this awesome OS
 - OSX     - Who knows, who cares :P



### How to run:

** Windows:
Install git: https://git-scm.com/downloads
- git clone https://github.com/JustAnAlias/kickstarter
- ![alt tag](https://github.com/JustAnAlias/kickstarter/blob/master/pictures/gitclone.png)
- open cmd and change directory to the kickstarter folder
- ![alt tag](https://github.com/JustAnAlias/kickstarter/blob/master/pictures/cd.png)
- vagrant up
- ![alt tag](https://github.com/JustAnAlias/kickstarter/blob/master/pictures/vagrantUp.png)





vagrant up
ssh into vm at 127.0.0.1:2222
user: vagrant
pass: vagrant

workon kickstarter
cd /code

Run our run script with
python run.py 

The run script will automaticly go through the process of Scraping kickstarter for the 40 most funded projects at the moment
It will then proceed to download any video that might be in the description of the projects.

When its done downloading videos, it will run our facedetection a video and take screenshots of the frames where faces is detected.
Next it will run watson's classifiers on the frames to see what is on the pictures.

## 
