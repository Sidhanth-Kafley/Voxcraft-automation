import os
import time
import json
import requests

#runs the julia file
os.system('julia inputs.jl')

#waits for base.vxa file to be created
while not os.path.exists("input/base.vxa"):
    time.sleep(1)

#upload the base.vxa to google drive
#this is where you add the access token from google playground
headers = {"Authorization": "Bearer ***access-token-goes-here***"}
para = {
    "name": "***file-name-goes-here***",
    "parents": [""]#this is where you add the id for the folder you are uploading
    #the base.vxa and robot.vxd files which you can get from the url in google drive
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': open("***file-path-goes-here***", "rb")#this is where you add your file path
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
print(r.text)

#waits for robot.vxd file to be created
while not os.path.exists("input/robot.vxd"):
	time.sleep(1)
#runs the yolo.py file which uploads the robot.vxd file to google drive
os.system('python3 yolo.py')

#waits for .history file to be downloaded from collab
while not os.path.exists("sample.history"):
	time.sleep(1)

#vizualizes the .history  file
os.system('Voxcraft-viz sample.history')

print("Done")
