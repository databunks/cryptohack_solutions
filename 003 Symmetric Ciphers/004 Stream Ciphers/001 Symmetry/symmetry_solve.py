import requests
import json
import string

def encrypt(plaintext, iv):
    plaintext = plaintext.encode("utf-8").hex()
    r = requests.get(f"https://aes.cryptohack.org/symmetry/encrypt/{plaintext}/{iv}/")
    return json.loads(r.text)["ciphertext"]

def encrypt_flag():
    r = requests.get("https://aes.cryptohack.org/symmetry/encrypt_flag/")
    return json.loads(r.text)["ciphertext"]

def brute_force_flag(encrypted_flag, iv):
    encrypted_flag = bytes.fromhex(encrypted_flag)
    flag = ""
    j = 0
    while True:
        for char in brute_force_chars:
            current_flag_bytes = bytes.fromhex(encrypt(flag + char, iv))
      
            if (current_flag_bytes[j] == encrypted_flag[j]):
                flag += char
                print(char)
                break
        j += 1
        if (flag[-1] == '}'):
            return flag

        



brute_force_chars = list(string.printable)

encrypted_flag = encrypt_flag()
iv = encrypted_flag[:32]
ciphertext = encrypted_flag[32:]

print(f"iv: {iv}\nciphertext: {ciphertext}\nencrypted flag (full): {encrypted_flag}\nencrypt function: {encrypt("crypto{", iv)}\n")

print(brute_force_flag(ciphertext, iv))