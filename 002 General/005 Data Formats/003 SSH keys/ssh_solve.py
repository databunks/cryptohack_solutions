from Crypto.PublicKey import RSA
import os



os.system('ssh-keygen -f bruce_rsa_6e7ecd53b443a97013397b1a1ea30e14.pub -e -m pem > bruce_RSA_PublicKey')

RSA_key_string = None
with open("bruce_RSA_PublicKey", "r") as f:
    RSA_key_string = f.read()

print(RSA.import_key(RSA_key_string).n)







