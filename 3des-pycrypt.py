#Encrypt text with PyCrypto 3DES module
#Michael, January 2014

from Crypto.Cipher import DES3
import hashlib
import string
import base64

print ('====== XEROCRYPT ======')
#Get plaintext message and round up to nearest 16 bytes
message = raw_input('MESSAGE: ')
length = 16 - (len(message) % 16)
message += chr(length)*length

#Get password and generate key as SHA256 digest
userPass = raw_input('KEY: ')
length = 16 - (len(userPass))
userPass += chr(length)*length

print (' ')
print ('[1] Encrypt - 3DES Mode')
print ('[2] Decrypt - 3DES Mode')
print (' ')
option = raw_input(': ')
print (' ')

if "1" in option:
		#Encrypt function
		EncryptData = DES3.new(userPass, DES3.MODE_CFB)
		ciphertext = EncryptData.encrypt(message)
		print ('CIPHERTEXT: ')
		print base64.b64encode(ciphertext)

else:
		#Decrypt function
		DecryptData = DES3.new(userPass, DES3.MODE_CFB)
		plaintext = DecryptData.decrypt(base64.b64decode(message))
		print ('DECRYPTED MESSAGE: ')
		print plaintext
