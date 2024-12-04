from Crypto.PublicKey import RSA


data = None
with open('privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a.pem', 'r') as file:
    data = Certificate.load(file.read())




print(RSA.import_key(data).d)