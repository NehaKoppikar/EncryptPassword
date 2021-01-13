from cryptography.fernet import Fernet

### Generate a Key
"""Commenting because the key changes every time"""
#key = Fernet.generate_key()
#print(key)

### Encrypt Password and Test Decrypting
key = b'ucuVFrkNcSkuq0rlQ9q_89Hcw28gtZOBXXxcmU0P1J8='
cipher_suite = Fernet(key)
ciphered_text = cipher_suite.encrypt(b"SuperSecretPassword")   #required to be bytes
print(ciphered_text)

### Validating Encrypted Password
ciphered_text = b'gAAAAABf_2uOJXqVmtQy9_hREoPofBEj99QXT45EHfqoO-JF40M6mWmm4IR6HQVfYhtizMVYpHoynWxvLqEaMa1TchRmLcJ_yb5_2tK-im-9gKZDnuX5s4k='
unciphered_text = (cipher_suite.decrypt(ciphered_text))
print(unciphered_text)

### Write Encrypted Password to a binary file
ciphered_text = cipher_suite.encrypt(b'SuperSecretpassword')
with open('mssqltip_bytes.bin', 'wb') as file_object:
    file_object.write(ciphered_text)

### Retrieve Encrypted password and Decrypt
with open('mssqltip_bytes.bin', 'rb') as file_object:
    for line in file_object:
        encryptedpwd = line
print(encryptedpwd)

### Decrypt Encrypted Password and Convert to string
uncipher_text = (cipher_suite.decrypt(encryptedpwd))
plain_text_encryptedpassword = bytes(uncipher_text).decode("utf-8") #convert to string
print(plain_text_encryptedpassword)