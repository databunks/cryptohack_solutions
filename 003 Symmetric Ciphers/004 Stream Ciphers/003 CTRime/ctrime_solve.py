import requests
import json
import string


def encrypt(plaintext):
    r = requests.get(f"https://aes.cryptohack.org/ctrime/encrypt/" + plaintext)
    return json.loads(r.text)["ciphertext"]


def CaptureFlag():

    flag = "crypto{"
    characters = string.printable

    while True:
        #exploit is based on the fact that invalid characters produce a different length string
        plaintext = (flag + '@') * 3 # multiplier is added to reduce the chance of length collisions
        ciphertext_base = encrypt(plaintext.encode('ascii').hex()) 
        
        for char in characters:
            ciphertext = encrypt(((flag + char) * 3).encode('ascii').hex())
            # Comparing if the base is bigger
            if len(ciphertext) < len(ciphertext_base):
                flag += char
                print(char)

                if char == "}":
                    return flag

                break

print(CaptureFlag())