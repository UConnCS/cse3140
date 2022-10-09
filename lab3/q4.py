from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes 
        
file_in = open('encrypted4.txt', 'rb')
iv = file_in.read(16)
original_data = file_in.read()
file_in.close()
file_in = open('.key.txt', 'rb')
variable = file_in.read()
file_in.close()

cipher = AES.new(variable, AES.MODE_CBC, iv=iv)
ciphered_data = cipher.decrypt(original_data)
print(ciphered_data)

file_out = open('Q4a', "wb")
file_out.write(cipher.iv)
file_out.write(ciphered_data)
file_out.close()