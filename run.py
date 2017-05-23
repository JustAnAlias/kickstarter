import subprocess

print("Executing Kickstarter.py")
subprocess.call("kickstarter.py", shell=True)
print("Finished")
print("Executing ks_video_downloader.py")
subprocess.call("ks_video_downloader.py", shell=True)
print("Finished")
print("Starting face detection with facedetect_2_proto.py")
subprocess.call("facedetect_2_proto.py", shell=True)
print("Finished face detection")
print("Starting Classification.py")
