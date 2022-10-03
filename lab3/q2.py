import os

h = "889eebf863379116db419a618271f0dd16d20f96dbf77b78346659bba20baf30"

for file in os.listdir("./Q1files"):
    if os.path.isfile(os.path.join("./Q1files", file)):
        sha256sum = os.system("sha256sum " + os.path.join("./Q1files", file))
        if h in sha256sum.strip():
            print(f"Hash matches file {file}")
            break