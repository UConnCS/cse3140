# This is an obfuscated ransomware file.
# To learn more about obfuscation, see the following links:
# https://searchsecurity.techtarget.com/definition/obfuscation
# https://www.geeksforgeeks.org/what-is-obfuscation/
# Your goal is to go through this funky code and understanmd what it is that it is doing,
# and how it is doing it.
# Once you understand how itis encrypting a user's file, werite a program (decrypt2.py)
# that decrpyts encrypted2.txt.

# This is the ransomware program that encrypts a specified file.
# Make sure you spend time to understand how it works.
# Feel free to change the input file to get a snesne of the programs capabilities.
# The given input program is an example .txt file, with several made up passwords.

# Use the following link to read documentation on this imported library:
# https://pycryptodome.readthedocs.io/en/latest/

import math
from Crypto.Cipher import AES
import binascii
from Crypto.Util.Padding import pad
import time
from Crypto.Random import get_random_bytes
from Crypto.Hash import MD5

BLOCKSIZE = 64
md5 = MD5.new()
count = 0

with open('R5.py', 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        count = count + 1
        md5.update(buf)
        buf = afile.read(BLOCKSIZE)

digest = md5.digest()
digest_copy = digest
digest_str = str(digest_copy)
key_file = '.key.txt'
file_out = open(key_file, "w")

# Write the varying length ciphertext to the file (this is the encrypted data)
file_out.write("")
file_out.close()
inputFile = 'p2.txt'  # Input file
out_file = 'e2e2.txt'  # outputted cipher text (can rename)
file_in = open(inputFile, 'rb')
file_in_data = file_in.read()

n = 23
f2 = 1
for i in range(1, n+1):
    f2 = f2 * i

file_in.close()
cipher = AES.new(digest_copy, AES.MODE_CBC)  # cipher
encrypted = cipher.encrypt(pad((file_in_data), AES.block_size))

file_out_result = open(out_file, "wb")
file_out_result.write(cipher.iv)
file_out_result.write(encrypted)
file_out_result.close()
print('OK')
