from fastapi import FastAPI, Request
import uvicorn
from gmail_utils import get_latest_emails, send_email
from calendar_utils import check_availability, create_event

app = FastAPI()

@app.post("/")
async def handle_mcp(request: Request):
    data = await request.json()
    command = data.get("input", "").lower()

    if "email" in command and "latest" in command:
        return {"output": get_latest_emails()}
    elif "availability" in command:
        return {"output": check_availability()}
    elif "schedule" in command:
        return {"output": create_event("Demo Meeting", "2025-06-08T14:00:00", attendees=["john@example.com"])}
    elif "send email" in command:
        return {"output": send_email("ha.doanmanh@gmail.com", "Subject", "This is a test email")}
    else:
        return {"output": "Command not recognized"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
