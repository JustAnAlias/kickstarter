![alt tag](https://github.com/JustAnAlias/kickstarter/blob/master/pictures/kickstarter-logo.png)

# How to use it:
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
