#Building on my previous example, this appends the hash value of the string
#to Passwords.txt.
#Michael, January 2014
#michael@ipv6secure.co.uk

import os
import hashlib

f = open('Passwords.txt', 'a')

txtPassword = raw_input("Enter password: ")
newPassword = hashlib.sha256(txtPassword).hexdigest()
f.write(newPassword)

