import os
import json
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

class GoogleSheetsAPI:
    def __init__(self, spreadsheet_id, range_name):
        self.spreadsheet_id = spreadsheet_id
        self.range_name = range_name
        self.credentials_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env', 'credentials.json')
        self.token_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env', 'token.json')
        self.scope = ['https://www.googleapis.com/auth/spreadsheets']
        self.credentials = self.get_credentials()
        self.service = self.build_service()

    def get_credentials(self):
        credentials = None
        if os.path.exists(self.token_file):
            credentials = Credentials.from_authorized_user_file(self.token_file)
        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_file, self.scope)
                credentials = flow.run_local_server()
            with open(self.token_file, 'w') as token:
                token.write(credentials.to_json())
        return credentials

    def build_service(self):
        return build('sheets', 'v4', credentials=self.credentials)

    def append_values(self, values):
        body = {'values': values}
        result = self.service.spreadsheets().values().append(
            spreadsheetId=self.spreadsheet_id,
            range=self.range_name,
            valueInputOption='RAW',
            body=body).execute()
        return result
    def read_values(self):
        result = self.service.spreadsheets().values().get(
            spreadsheetId=self.spreadsheet_id,
            range=self.range_name).execute()
        values = result.get('values', [])
        return values

def main():
    SPREADSHEET_ID = '19zmhOoTsvOdYkCdLGDKepqmKgVoneVQWcprp72wxCXw'
    RANGE_NAME = 'Sheet1!A1:C5'

    sheets_api = GoogleSheetsAPI(SPREADSHEET_ID, RANGE_NAME)
    # Read values from the sheet
    values_read = sheets_api.read_values()
    if values_read:
        print("Values read from the sheet:")
        for row in values_read:
            print(row)
    else:
        print("No data found in the sheet.")

if __name__ == '__main__':
    main()
