# A simple Pythn script that hashes an input string
#Michael, January 2014
#michael@ipv6secure.co.uk

import os
import hashlib

txtPassword = raw_input("Enter password: ")
print hashlib.sha256(txtPassword).hexdigest()


