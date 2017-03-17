#Encrypt text with PyCrypto AES module
#Michael, January 2014

from Crypto.Cipher import AES
import hashlib
import string
import base64

print ('[1] Encrypt')
print ('[2] Decrypt')
option = raw_input(': ')

if "1" in option:
		#Get plaintext message and round up to nearest 16 bytes
		message = raw_input('MESSAGE: ')
		length = 16 - (len(message) % 16)
		message += chr(length)*length

		#Get password and generate key as SHA256 digest
		Pass = raw_input('KEY: ')
		encodedPass = hashlib.sha256(Pass).digest()

		#Encrypt function
		EncryptData = AES.new(encodedPass, AES.MODE_ECB)
		ciphertext = EncryptData.encrypt(message)
		print base64.b64encode(ciphertext)

else:
		Pass = raw_input('KEY: ')
		encodedPass = hashlib.sha256(Pass).digest()

		message = raw_input('CIPHERTEXT: ')
		length = 16 - (len(message) % 16)
		message += chr(length)*length

		#Decrypt function
		DecryptData = AES.new(encodedPass, AES.MODE_ECB)
		plaintext = DecryptData.decrypt(base64.b64decode(message))
		print plaintext
