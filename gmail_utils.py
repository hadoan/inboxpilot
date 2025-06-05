import imaplib
import smtplib
import email
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.getenv("EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")

def get_latest_emails(limit=5):
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(EMAIL, APP_PASSWORD)
    mail.select("inbox")
    result, data = mail.search(None, "ALL")
    ids = data[0].split()[-limit:]
    messages = []
    for email_id in reversed(ids):
        result, msg_data = mail.fetch(email_id, "(RFC822)")
        raw_email = msg_data[0][1]
        msg = email.message_from_bytes(raw_email)
        # Safely extract text content from multipart or plain messages
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))
                if content_type == "text/plain" and "attachment" not in content_disposition:
                    body = part.get_payload(decode=True).decode(errors="ignore")
                    break
        else:
            body = msg.get_payload(decode=True)
            if body:
                body = body.decode(errors="ignore")

        messages.append({
            "from": msg["From"],
            "subject": msg["Subject"],
            "snippet": body[:150] if body else ""
        })
    mail.logout()
    return messages

def send_email(to, subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL
    msg["To"] = to
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL, APP_PASSWORD)
        server.send_message(msg)
    return "Email sent."
