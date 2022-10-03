import os
import hashlib

from time import time

start = time()
cracked = {}
pairs = []
names = []

print(f"Start time: {start}")

with open("../gang.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line:
            names.append(line)

with open('HashedPWs', 'r') as f:
    pairs = [(split[0], split[1]) for line in f for split in [line.split(',')] if split[0] in names]

for pair in pairs:
    user = pair[0]
    found = False
    
    with open('../PwnedPWs100k.txt', 'r') as f:
        while True:
            if found:
                break
            line = f.readline().strip()
            for i in range(0, 10):
                for j in range(0, 10):
                    guess = f"{line}{i}{j}"
                    h = hashlib.sha256()
                    h.update(bytes(guess, 'utf-8'))
                    digest = h.hexdigest()

                    # print(f"Trying {user}:{guess} | {pair[1]} {'==' if pair[1] == digest else '!='} {digest}\n")

                    if (digest == pair[1]):
                        cracked[user] = guess
                        print(f"Cracked {user} with {guess}")
                        found = True
                        break

print(f"Time taken: {time() - start}s")
print(f"End time: {time()}")

with open('A5', 'w') as f:
    for username, password in cracked.items():
        f.write(f"{username},{password}")