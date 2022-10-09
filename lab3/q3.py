import os
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15

key = RSA.import_key(open("./PublicKey.pem", "rb").read())

for file in os.listdir("./Q3files"):
    if os.path.isfile(os.path.join("./Q3files", file)):
        with open(os.path.join("./Q3files", file), "rb") as f:
            data = f.read()
        digest = SHA256.new(data)
        try:
            pkcs1_15.new(key).verify(digest, data)
            print(f"Signature match: {file}")
            break
        except (ValueError, TypeError):
            print(f"Signature does not match file {file}")