"""Utility to upload a local CSV file to Google Sheets using a service account.

Usage notes:
- Create a Google Cloud service account and download the JSON key file (credentials.json).
- Share the target spreadsheet with the service account email (if using an existing spreadsheet).
- Optionally set the environment variable GOOGLE_SHEETS_SPREADSHEET_ID to the target spreadsheet ID.
- Install dependencies from requirements.txt: `pip install -r requirements.txt`.

The main function is `upload_csv_to_google_sheets(csv_path, spreadsheet_id=None, sheet_name='Sheet1', creds_path='credentials.json')`.
"""
import os
import csv
from datetime import datetime

try:
    import gspread
except Exception:  # pragma: no cover - import-time
    gspread = None


def upload_csv_to_google_sheets(csv_path, spreadsheet_id=None, sheet_name='Sheet1', creds_path='credentials.json'):
    """Upload a CSV to a Google Sheets worksheet.

    Args:
        csv_path (str): Path to the local CSV file.
        spreadsheet_id (str|None): Google Sheets spreadsheet ID. If None, will try the
            environment variable GOOGLE_SHEETS_SPREADSHEET_ID. If still None, the function
            will attempt to create a new spreadsheet (this requires the Drive API scope in
            the service account credentials).
        sheet_name (str): Worksheet name to write into. If it doesn't exist it will be created.
        creds_path (str): Path to the service account JSON credentials file.

    Returns:
        str: URL of the spreadsheet on success.

    Raises:
        RuntimeError: If gspread not installed or upload fails.
        FileNotFoundError: If the CSV or credentials file is missing.
    """
    if gspread is None:
        raise RuntimeError("gspread is not installed. Run: pip install gspread google-auth")

    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    if not os.path.exists(creds_path):
        raise FileNotFoundError(f"Credentials file not found: {creds_path}. Create a service account JSON and save it as this path.")

    # Prefer explicit spreadsheet_id, then environment variable
    if spreadsheet_id is None:
        spreadsheet_id = os.environ.get('GOOGLE_SHEETS_SPREADSHEET_ID')

    # Create authenticated client
    client = gspread.service_account(filename=creds_path)

    sheet = None
    if spreadsheet_id:
        try:
            sheet = client.open_by_key(spreadsheet_id)
        except Exception as e:
            raise RuntimeError(f"Unable to open spreadsheet with id {spreadsheet_id}: {e}")
    else:
        # Create a new spreadsheet - note this requires Drive scopes in the credentials
        title = f"CSV Upload - {os.path.basename(csv_path)} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        try:
            sheet = client.create(title)
            # attempt to open it by id (client.create returns a Spreadsheet instance)
            spreadsheet_id = sheet.id
        except Exception as e:
            raise RuntimeError(f"Failed to create new spreadsheet: {e}")

    # Ensure worksheet exists, then upload
    try:
        try:
            worksheet = sheet.worksheet(sheet_name)
        except gspread.exceptions.WorksheetNotFound:
            worksheet = sheet.add_worksheet(title=sheet_name, rows="1000", cols="20")

        # Read CSV
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)

        # Clear existing content and update from A1
        worksheet.clear()
        # gspread's update accepts a list of lists starting at A1
        worksheet.update('A1', rows)

        url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}"
        print(f"CSV '{csv_path}' uploaded to Google Sheets: {url}")
        return url
    except Exception as e:
        raise RuntimeError(f"Failed to upload CSV to Google Sheets: {e}")
