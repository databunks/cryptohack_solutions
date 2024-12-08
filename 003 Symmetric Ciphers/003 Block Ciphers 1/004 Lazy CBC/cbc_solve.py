import requests
import json

def encrypt(plaintext):
    r = requests.get("https://aes.cryptohack.org/lazy_cbc/encrypt/" + plaintext)
    return json.loads(r.text)

# def getCiphertext():
#     r = requests.get("https://aes.cryptohack.org/flipping_cookie/get_cookie/")
#     return json.loads(r.text)["ciphertext"]


print(encrypt("h" * 16))