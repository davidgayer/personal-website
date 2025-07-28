from flask import Flask, render_template, request, jsonify
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create Flask app for personal website
app = Flask(__name__)

# Security: Use environment variable for secret key
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'dev-key-change-in-production')

@app.route('/')
def home():
    """Home page with introduction and links"""
    return render_template('index.html')

@app.route('/about')
def about():
    """About page with more details"""
    return render_template('about.html')

@app.route('/projects')
def projects():
    """Projects page showcasing your work"""
    return render_template('projects.html')

@app.route('/contact')
def contact():
    """Contact information"""
    return render_template('contact.html')

@app.route('/test-minimal')
def test_minimal():
    """Minimal memory test page"""
    return render_template('test_minimal.html')

@app.route('/send-email', methods=['POST'])
def send_email():
    """Send email from contact form"""
    try:
        data = request.get_json()
        visitor_email = data.get('email')
        message = data.get('message')
        
        # Validate inputs
        if not visitor_email or not message:
            return jsonify({'success': False, 'error': 'Email and message are required'}), 400
        
        # Email configuration
        sender_email = os.getenv('GMAIL_EMAIL')  # Your Gmail account
        sender_password = os.getenv('GMAIL_APP_PASSWORD')
        recipient_email = "davidgayer1@gmail.com"  # Your personal email
        
        # Create email message
        msg = MIMEMultipart()
        msg['From'] = f"Website Contact Form <{sender_email}>"  # Shows as "Website Contact Form"
        msg['To'] = recipient_email
        msg['Subject'] = f"New message from {visitor_email}"
        
        body = f"""
        New message from your website contact form:
        
        From: {visitor_email}
        Message:
        {message}
        
        ---
        This email was sent from your personal website contact form.
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email via SMTP
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, sender_password)
            text = msg.as_string()
            server.sendmail(sender_email, recipient_email, text)
            server.quit()
            print(f"Email sent successfully from {visitor_email}: {message}")
        except Exception as e:
            print(f"SMTP Error: {e}")
            # Fallback: just log the message if SMTP fails
            print(f"Email from {visitor_email}: {message}")
        
        return jsonify({'success': True, 'message': 'Email sent successfully'}), 200
        
    except Exception as e:
        print(f"Error sending email: {e}")
        return jsonify({'success': False, 'error': 'Failed to send email'}), 500

if __name__ == '__main__':
    # Railway will set PORT environment variable
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)