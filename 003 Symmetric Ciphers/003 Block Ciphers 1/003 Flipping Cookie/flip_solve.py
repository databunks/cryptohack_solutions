import requests
import json
import os
import binascii
from datetime import datetime, timedelta

def getCookie():
    r = requests.get("https://aes.cryptohack.org/flipping_cookie/get_cookie/")
    return json.loads(r.text)["cookie"]

def checkAdmin(cookie, iv):
    r = requests.get("https://aes.cryptohack.org/flipping_cookie/check_admin/" + cookie + '/' + iv )
    return json.loads(r.text)


def flip_bits(cookie):
    expiry_date = (datetime.today() + timedelta(days=1)).strftime("%s") # reconstructing expiry date
    plaintext = ("admin=False;expiry=" + expiry_date).encode() # reconstructing plaintext
    iv = [1] * 16 # injecting our custom initialization vector
    ciphertext_payload = list(cookie)
    plaintext_payload = b';admin=True;' #plaintext payload for verifcation bypass

    for i in range(0, len(plaintext_payload)):
       # flip bits
       ciphertext_payload[16 + i] = plaintext[16 + i] ^ plaintext_payload[i] ^ cookie[16+i]
       iv[i] = plaintext[i] ^ plaintext_payload[i] ^ cookie[i]

    ciphertext_payload = bytes(ciphertext_payload).hex()
    iv = bytes(iv).hex()
    return [ciphertext_payload, iv]

cookie = getCookie()
payload = flip_bits(bytes.fromhex(getCookie()))
print(checkAdmin(cookie=payload[0], iv=payload[1]))