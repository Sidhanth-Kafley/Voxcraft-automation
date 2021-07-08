import json
import requests
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
