from flask import Flask, render_template
import os

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

if __name__ == '__main__':
    # Railway will set PORT environment variable
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)