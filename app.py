from flask import Flask, render_template
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
import os

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'default_secret_key')

@app.route('/')
def home():
    return render_template('index.html')  # Serve index.html

# Define the handler for Netlify functions (Serverless)
def handler(event, context):
    # Wrap the Flask app with DispatcherMiddleware to integrate with Netlify
    return DispatcherMiddleware(app.wsgi_app, {
        '/.netlify/functions/handler': app
    })(event, context)

# For local testing (when running locally, it will run via werkzeug)
if __name__ == "__main__":
    run_simple('0.0.0.0', 5000, app)
