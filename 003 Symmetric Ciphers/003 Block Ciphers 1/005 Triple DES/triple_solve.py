import requests
import json

def encrypt(key, plaintext):
    try:
        r = requests.get(f"https://aes.cryptohack.org/triple_des/encrypt/{key}/{plaintext}/")
        return json.loads(r.text)["ciphertext"]
    except:
        print("Failed to make request")

def encrypt_flag(key):
    try:
        r = requests.get(f"https://aes.cryptohack.org/triple_des/encrypt_flag/{key}")
        return json.loads(r.text)["ciphertext"]
    except:
        print("Failed to make request")

key_list = []
for i in range(0, 255):
    key_list.append(i.to_bytes())

def bruteForceKey():
    for i in key_list:
        for j in key_list:
            key = i * 8 + j * 8
            flag = encrypt_flag(key.hex())
            cipher = encrypt(key.hex(), flag)
            if (cipher is not None):
                print(bytes.fromhex(cipher))
                if (bytes.fromhex(cipher).decode('latin-1').startswith('crypto{')):
                    print(bytes.fromhex(cipher).decode('utf-8'))
                    return


bruteForceKey()