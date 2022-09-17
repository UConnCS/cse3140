import subprocess
import sys
from time import time

start = time()
print(f"Start time: {start}")

pairs = {}

with open("../gang.txt", "r") as f:
    for member in f:
        pairs[member.strip()] = "?"

    pairs["Vlad"] = "XuanYqUE"
    pairs["Al"] = "ePcsjmet"
    pairs["Andrew"] = "vwQdfOdY"

    with open("./PwnedPWfile") as f:
        for entry in f:
            _name, pw = entry.split(",")
            password = pw.strip()
            for member in list(filter(lambda x: pairs[x] == '?', pairs)):
                if 'successful' in str(subprocess.check_output(["python3", "Login.pyc", member, password])).lower():
                    print(f"Found {member}:{password}")
                    pairs[member] = password
                    continue

    for (name, password) in pairs.items():
        print(f"{name},{password}")

    print(f"End time: {str(time())}")
    print(f"Time taken: {str(time() - start)}ms")