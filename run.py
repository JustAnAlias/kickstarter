import kickstarter
from ks_video_downloader import VideoDownloader

print("Executing Kickstarter.py")
kickstarter.run()
print("Finished")
print("Executing ks_video_downloader.py")
downloader = VideoDownloader()
downloader.run()
print("Finished")
print("Starting face detection with facedetect_2_proto.py")
#facedetect_2_proto.run()
print("Finished face detection")
print("Starting Classification.py")
