#Michael, January 2014
#Need PythonCard and PyCrypto modules installed

"""
__version__ = "$Revision: 1.5 $"
__date__ = "$Date: 2004/04/30 16:26:12 $"
"""

from PythonCard import model
from Crypto.Cipher import AES
import hashlib
import string
import base64

class MyBackground(model.Background):

    def on_initialize(self, event):
        # if you have any initialization
        # including sizer setup, do it here
        pass

 #The Encrypt button
    def on_cmdEncrypt_mouseClick(self, event):
        #Get plaintext message and round up to nearest 16 bytes
		message = self.components.txtMessage.text
		length = 16 - (len(message) % 16)
		message += chr(length)*length

		#Get password and generate key as SHA256 digest
		Pass = self.components.txtPass.text
		encodedPass = hashlib.sha256(Pass).digest()

		#Encrypt function
		EncryptData = AES.new(encodedPass, AES.MODE_ECB)
		ciphertext = EncryptData.encrypt(message)
		self.components.txtMessage.text = base64.b64encode(ciphertext)
        
    #The Decrypt button
    def on_cmdDecrypt_mouseClick(self, event):
        Pass = self.components.txtPass.text
        encodedPass = hashlib.sha256(Pass).digest()

		#Pad text message to the nearest 16 bytes.
        message = self.components.txtMessage.text
        length = 16 - (len(message) % 16)
        message += chr(length)*length

		#Decrypt function
        DecryptData = AES.new(encodedPass, AES.MODE_ECB)
        self.components.txtMessage.text = DecryptData.decrypt(base64.b64decode(message))
		
if __name__ == '__main__':
    app = model.Application(MyBackground)
    app.MainLoop()
