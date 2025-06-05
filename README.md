# 📬 InboxPilot - Email & Calendar Agent MCP Tool

**Track:** `mcp-server-track`  
**Type:** FastAPI MCP Tool

InboxPilot is a local MCP-compatible server that enables AI agents to:
- 📥 Summarize your latest Gmail emails
- 📤 Draft and send emails
- 📅 Check your Google Calendar availability
- 🗓️ Schedule meetings automatically

---

## 🚀 Features

- `latest emails`: Fetch the 5 most recent messages from Gmail
- `send email`: Draft and send a test email
- `check availability`: Retrieve free/busy times from Google Calendar
- `schedule meeting`: Schedule a 30-minute event

---

## ⚙️ Setup Instructions

### 1. 📧 Configure Gmail (App Password)
To access Gmail using IMAP/SMTP:

1. Enable 2-Step Verification for your Google Account
2. Go to [Google App Passwords](https://myaccount.google.com/apppasswords)
3. Choose **Mail** > **Other (Custom name)**, call it `InboxPilot`
4. Copy the **16-character app password**
5. Open `gmail_utils.py` and update:
   ```python
   EMAIL = "your_email@gmail.com"
   APP_PASSWORD = "your_16_char_app_password"
   ```

---

### 2. 📆 Configure Google Calendar (OAuth)

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project and enable the **Google Calendar API**
3. Go to **APIs & Services > Credentials**
4. Click **"Create Credentials" → "OAuth Client ID"**
5. Choose **Application type**: `Desktop app`
6. Download the `credentials.json` file
7. Place it in the root of your project folder
8. Install dependencies:
   ```bash
   pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
   ```
9. Run the authorization flow:
   ```bash
   python calendar_auth.py
   ```
   This will generate `token.json`

---

### 3. ▶️ Run the MCP Tool Server

Start the FastAPI server:
```bash
python mcp_server.py
```

You should see:
```
Running on http://127.0.0.1:7860
```

---

## 🧪 Testing the MCP Tool

Send test JSON input with `curl`:
```bash
curl -X POST http://127.0.0.1:8000/      -H "Content-Type: application/json"      -d '{"input": "check latest email"}'
```

Try changing the `input` to:
- `"latest emails"`
- `"send email to someone@example.com"`
- `"check availability next week"`
- `"schedule meeting"`

---

## 🛠 Dependencies

Install them with:

```bash
pip install -r requirements.txt
```

---

## 🧠 Notes

- This tool is local-only by default. No data is shared externally.
- You can expose it publicly (for agent testing) using `ngrok`, `gradio.share`, or deploy it to Hugging Face Spaces.

---

## 💬 Need Help?

Create an issue or ping us on Discord in the `agents-mcp-hackathon` channel!
