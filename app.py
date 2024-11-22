from flask import Flask, jsonify, render_template
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
import os

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'default_secret_key')

@app.route('/')
def home():
    return render_template("index.html")

# Wrap the Flask app in the Vercel function handler
def handler(event, context):
    return DispatcherMiddleware(app.wsgi_app, {
        '/.netlify/functions/handler': app
    })(event, context)

# Local testing (if needed)
if __name__ == "__main__":
    run_simple('0.0.0.0', 5000, app)
