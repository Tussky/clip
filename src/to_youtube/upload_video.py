import os

from apiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow

import json
# loading in api key
SECRET_FILE = "secrets.json"
with open("client_secret.json") as secrets:
    my_secrets = json.load(secrets)

api_key = my_secrets['installed']['client_secret']
client_id = my_secrets['installed']['client_id']


youtube = build("youtube", "v3", developerKey = api_key) 

request = youtube.channels().list(part="snippet", id =client_id) 

response = request.execute()
print(response)
