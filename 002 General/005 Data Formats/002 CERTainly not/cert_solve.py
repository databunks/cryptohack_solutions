from asn1crypto.x509 import Certificate

cert = None

with open("2048b-rsa-example-cert_3220bd92e30015fe4fbeb84a755e7ca5.der", "rb") as f:
    cert = Certificate.load(f.read())

cert_modulus = cert.public_key.native["public_key"]["modulus"]

print("{:#d}".format(cert_modulus))