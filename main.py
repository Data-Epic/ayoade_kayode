import os
import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
from generate_csv import data



load_dotenv()


from os.path import expanduser

CREDENTIALS_PATH = expanduser("~/Desktop/gspread_workspace/gspreadsheet1.json")


SPREADSHEET_TITLE = os.getenv("SPREADSHEET_TITLE")
CREDENTIALS_PATH = os.getenv("CREDENTIALS_PATH")



# Authenticate with Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_PATH, scope)
client = gspread.authorize(credentials)

# Open the Google Spreadsheet using its title
spreadsheet_title = SPREADSHEET_TITLE
sh = client.open(spreadsheet_title)

# Select the worksheet by its index (0-based)
worksheet = sh.get_worksheet(0)

# Read data from CSV file
data = []
with open("data.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        data.append(row)

# Update the worksheet with the data
worksheet.update("A1", data)

print("Data successfully written to the spreadsheet!")




print("Current working directory:", os.getcwd())
