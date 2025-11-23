from apiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow

# YT API key and authentication credentials
from my_youtube_secrets import YT_OAUTHKEY, YT_API_KEY 

# building YT object and listing snippets
youtube = build("youtube", "v3", developerKey = YT_API_KEY) 
request = youtube.channels().list(part="snippet", id = YT_OAUTHKEY) 
response = request.execute()
print(response)


media = MediaFileUpload("../../vids/tester_vid")
# Attempting to upload a video
# upload = youtube.videos().upload()

body = {
        "snippet": {
            "title": "hi",
            "description":"fun games",
            "tags" : "fun",
        }
}

upload_request = youtube.videos().insert(
    part = "snippet,status",
    body = body,
    media_body = media,
)
print("created upload request")
upload_response = upload_request.execute()
print(upload_response)
