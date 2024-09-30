
# -*- cofing: utf-8 -*-
import argparse
import hashlib

# parsing
psr = argparse.ArgumentParser(description='hashing given password')
psr.add_argument('password', help='input password you want to hash')
psr.add_argument('-t', '--type', default='sha256',choices=['sha256', 'sha512', 'md5'] )
args = psr.parse_args() 

# hashing given password
password = args.password
hashtype = args.type
m = getattr(hashlib,hashtype)()
m.update(password.encode())

# output
print("< hash-type : " + hashtype + " >")
print(m.hexdigest())
