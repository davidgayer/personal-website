# Email Setup Guide

## Step 1: Get Gmail App Password

1. **Go to Google Account Settings:**
   - Visit: https://myaccount.google.com/
   - Sign in with your Gmail account

2. **Enable 2-Step Verification:**
   - Click "Security" in left sidebar
   - Find "2-Step Verification" and enable it
   - Follow the setup process (usually involves your phone)

3. **Create App Password:**
   - Go back to "Security"
   - Find "App passwords" (appears after enabling 2-Step Verification)
   - Click "App passwords"
   - Select "Mail" from dropdown
   - Click "Generate"
   - **Copy the 16-character password** (looks like: `abcd efgh ijkl mnop`)

## Step 2: Create .env File

Create a file called `.env` in your project root with this content:

```
GMAIL_EMAIL=davidgayer@gmail.com
GMAIL_APP_PASSWORD=your-16-char-app-password-here
```

**Replace `your-16-char-app-password-here` with the actual 16-character password you copied.**

## Step 3: Test the Contact Form

1. Start your Flask app: `python app.py`
2. Go to your contact page
3. Fill out the contact form
4. Submit - you should receive an email!

## Security Notes

- **Never commit the .env file to git** (it's already in .gitignore)
- **Keep your app password secure** - don't share it
- **The .env file is for local development only**

## Troubleshooting

- **"Username and Password not accepted"** = Wrong app password
- **"2-Step Verification not enabled"** = Enable it first
- **"App passwords not available"** = Enable 2-Step Verification first 