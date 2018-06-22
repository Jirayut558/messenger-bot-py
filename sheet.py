"""
Shows basic usage of the Sheets API. Prints values from a Google Spreadsheet.
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# Setup the Sheets API
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('sheets', 'v4', http=creds.authorize(Http()))

def read_sheet_data():
    # Call the Sheets API
    SPREADSHEET_ID = '18nMU0OLobktA3AowOSdWXGByfipdj5Xk9Y4tvbxHnnw'
    RANGE_NAME = 'A:B'
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                                 range=RANGE_NAME).execute()
    values = result.get('values', [])
    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[1]))

def write_sheet_data(text_input):
    SPREADSHEET_ID = '18nMU0OLobktA3AowOSdWXGByfipdj5Xk9Y4tvbxHnnw'
    RANGE_NAME = 'NewNoi!A:A'

    values = [["new value"]]
    body = {
        'values': text_input
    }
    result = service.spreadsheets().values().append(
        spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME,
        valueInputOption="USER_ENTERED", body=body).execute()
    print('{0} cells appended.'.format(result \
                                       .get('updates') \
                                       .get('updatedCells')));
if __name__ == '__main__':
    write_sheet_data()