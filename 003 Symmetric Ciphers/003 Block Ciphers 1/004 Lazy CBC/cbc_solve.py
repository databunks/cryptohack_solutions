import requests
import json

def encrypt(plaintext):
    r = requests.get("https://aes.cryptohack.org/lazy_cbc/encrypt/" + plaintext)
    return json.loads(r.text)["ciphertext"]


def receive(ciphertext):
    r = requests.get("https://aes.cryptohack.org/lazy_cbc/receive/" + ciphertext)
    return json.loads(r.text)

def getFlag(key):
    r = requests.get("https://aes.cryptohack.org//lazy_cbc/get_flag/" + key)
    return json.loads(r.text)


def xor_hex(hex1, hex2):
    return hex(int(hex1, 16) ^ int(hex2, 16))[2:]


# AES-CBC Decryption process:
#
# key = iv = decrypt(cipher_block_0) ^ plaintext_block_0
# plaintext_block_0 = decrypt(cipher_block_0) ^ iv
# plaintext_block_1 = decrypt(cipher_block_1) ^ cipher_block_0
# plaintext_block_2 = decrypt(cipher_block_2) ^ cipher_block_1
# 
# The IV gets used as a key as well which is the weakness here
#
# We can reduce the equation to:
# plaintext_block_0 ^ plaintext_block_2 = iv = key
# since we make cipher_block_1 = 0 in our payload:

payload = ("8b" * 16) + ("00" * 16) +  ("8b" * 16)
decrypted_ciphertext = receive(payload)["error"].split(': ')[1]
key = xor_hex(decrypted_ciphertext[:32], decrypted_ciphertext[64:])
print(bytearray.fromhex(getFlag(key)["plaintext"]).decode('utf-8'))

