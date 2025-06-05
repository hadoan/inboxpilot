
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from datetime import datetime, timedelta

SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_service():
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    return build('calendar', 'v3', credentials=creds)

def check_availability(days=5):
    service = get_service()
    now = datetime.utcnow().isoformat() + 'Z'
    end = (datetime.utcnow() + timedelta(days=days)).isoformat() + 'Z'
    events_result = service.events().list(calendarId='primary', timeMin=now, timeMax=end, singleEvents=True, orderBy='startTime').execute()
    events = events_result.get('items', [])
    availability = [{"start": e["start"].get("dateTime", e["start"].get("date")),
                     "end": e["end"].get("dateTime", e["end"].get("date"))} for e in events]
    return availability

def create_event(summary, start_time, duration=30, attendees=[]):
    service = get_service()
    end_time = (datetime.fromisoformat(start_time) + timedelta(minutes=duration)).isoformat()
    event = {
        'summary': summary,
        'start': {'dateTime': start_time, 'timeZone': 'UTC'},
        'end': {'dateTime': end_time, 'timeZone': 'UTC'},
        'attendees': [{'email': email} for email in attendees]
    }
    created = service.events().insert(calendarId='primary', body=event).execute()
    return f"Event created: {created.get('htmlLink')}"
