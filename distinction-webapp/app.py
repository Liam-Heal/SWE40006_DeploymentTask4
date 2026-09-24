import os
from flask import Flask

app = Flask(__name__)

SITE_MESSAGE = os.environ.get('SITE_MESSAGE', 'Default message - no environment variable set')

@app.route('/')
def home():
    return f"""
    <h1>SWE40006 Deployment Task 4 - Distinction Level</h1>
    <p>This is a custom Flask web application running in an optimized Docker container.</p>
    <p><strong>Environment message:</strong> {SITE_MESSAGE}</p>
    <p><a href="/about">About this app</a></p>
    """

@app.route('/about')
def about():
    return "<h2>About</h2><p>Built for SWE40006 Software Deployment and Evolution, Task 4.3.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)