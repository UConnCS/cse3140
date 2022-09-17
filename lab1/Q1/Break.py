import subprocess
import sys
from time import time

start = time()
print(f"Start time: {start}")
with open("../MostCommonPWs.txt") as f:
    for line in f:
        line = line.strip()
        if subprocess.call(["python3", "Login.pyc", "Adam", line]) == 0:
            print(f"Correct password is: {line}")
            print(f"End time: {str(time())}")
            print(f"Time taken: {str(time() - start)}ms")
            sys.exit(0)