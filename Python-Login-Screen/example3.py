#The script buffers the password file created in Example 2, hashes a string and 
#uses that hash value as a search term. #If there's a match, exit() forces the 
#program to terminate before printing the Login Fail message.
#Michael, January 2014
#michael@ipv6secure.co.uk

import os, sys
import hashlib
import string
import re

#Set hash value of user input as the search term
txtPassword = raw_input("Enter password: ")
searchKey = hashlib.sha256(txtPassword).hexdigest()

#Buffer the password file
lines = open("Passwords.txt", "r" ).readlines()

#Search lines in password file for a match
for line in lines:
    if re.search(searchKey, line ):
	print "Login Success"
	exit()
print "Login Fail"
