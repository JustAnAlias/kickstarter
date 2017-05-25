import kickstarter
import failedd
from ks_video_downloader import VideoDownloader
import facedetect
import facedetect_2_proto
import classifier

print("Executing Kickstarter.py")
kickstarter.run()
print("Getting failed projects as well from failedd")
failedd.run()
print("Executing ks_video_downloader.py")
downloader = VideoDownloader()
downloader.run()
print("Finished")
print("Starting face detection with facedetect_2_proto.py")
facedetect_2_proto.run()
print("Finished face detection")
print("Starting Classifier.py")
classifier.run()
print("classifiers saved)
