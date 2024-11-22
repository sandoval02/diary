from flask import Flask, render_template
import os

# Initialize the Flask application
app = Flask(__name__)

# Set the secret key for Flask sessions
app.secret_key = os.getenv('SECRET_KEY', 'default_secret_key')

# Define the home route
@app.route("/")
def home():
    return render_template("index.html")  # Render index.html from the 'templates' directory

# For local development
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
