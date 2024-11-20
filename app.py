from waitress import serve
import os
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'default_secret_key')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Use Waitress to serve the app in production
    serve(app, host='0.0.0.0', port=5000)
