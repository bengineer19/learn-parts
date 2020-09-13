import json
import os
import io
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload

from exceptions import InvalidInfoException

service_account_info = json.loads(os.getenv('GDRIVE_AUTH'))
# SCOPES = [
#     'https://www.googleapis.com/auth/drive.metadata.readonly',
#     'https://www.googleapis.com/auth/drive.file'
# ]
SCOPES = [
    'https://www.googleapis.com/auth/drive'
]

creds = service_account.Credentials.from_service_account_info(
        service_account_info, scopes=SCOPES)

service = build('drive', 'v3', credentials=creds)


def list_files_in_folder(folder_id):
    ''' Returns generator of (file_name, file_id) '''
    page_token = None
    while True:
        query = f"'{folder_id}' in parents"
        response = service.files().list(q=query,
                                        spaces='drive',
                                        fields='nextPageToken, files(id, name)',
                                        pageToken=page_token).execute()
        for file in response.get('files', []):
            # Process change
            yield (file.get('name'), file.get('id'))
        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break



def get_song(folder_id):
    # Load credentials from json string in GDRIVE_AUTH env var
    files = list(list_files_in_folder(folder_id))
    if not 'info.json' in [f_name for f_name, f_id in files]:
        raise InvalidInfoException("No info file found")


    return {}


def get_file(file_id):
    # file_id = '0BwwA4oUTeiV1UVNwOHItT0xfa2M'
    request = service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print(f"Download {int(status.progress() * 100)}")

    fh.seek(0)
    return fh