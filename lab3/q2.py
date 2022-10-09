import os
import subprocess

h = "5c01e943db42684800123d6b1598c7e9efbc8e9050becaec1c4536f6e1c50907"

for file in os.listdir("./Q2files"):
    if os.path.isfile(os.path.join("./Q2files", file)):
        sha256sum = subprocess.check_output(["sha256sum", os.path.join("./Q2files", file)])
        if h in sha256sum.decode("utf-8"):
            print(f"Hash matches file {file}")
            break