import gspread

def authenticate():
    # Authenticate with Google using the Service Account credentials
    gc = gspread.service_account(filename="gspreadsheet1.json")
    return gc
