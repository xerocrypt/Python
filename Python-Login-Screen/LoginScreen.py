"""
__version__ = "$Revision: 1.5 $"
__date__ = "$Date: 2004/04/30 16:26:12 $"
"""

from PythonCard import dialog, model
import os, sys
import hashlib
import string
import re

class MyBackground(model.Background):

    def on_initialize(self, event):
        # if you have any initialization
        # including sizer setup, do it here
        pass

    #Password set button
    def on_cmdSetPassword_mouseClick(self, event):
        f = open('Passwords.txt', 'a')
        newPassword = hashlib.sha256(self.components.txtPassword.text).hexdigest()
        f.write(newPassword)
                
        dialog.alertDialog(self, 'Password Set')


    #The login button
    def on_cmdLogin_mouseClick(self, event):
        searchKey = hashlib.sha256(self.components.txtPassword.text).hexdigest()
        #Buffer the password file
        lines = open("Passwords.txt", "r" ).readlines()

        #Search lines in password file for a match
        for line in lines:
            if re.search(searchKey, line ):
                dialog.alertDialog(self, 'Login Success')
        
    #The hash button
    def on_cmdCancel_mouseClick(self, event):
        self.components.txtHash.text = hashlib.sha256(self.components.txtPassword.text).hexdigest()
        
if __name__ == '__main__':
    app = model.Application(MyBackground)
    app.MainLoop()
