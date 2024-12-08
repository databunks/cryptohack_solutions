from binascii import hexlify
import requests
import json
import string


def encrypt(plaintext_bytes):
    plaintext = hexlify(plaintext_bytes).decode()
    r = requests.get("http://aes.cryptohack.org/ecb_oracle/encrypt/"+ plaintext)
    return (json.loads(r.text))['ciphertext']



block_size = 31
characters = list(string.ascii_letters) + ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '_', '{', '}']


def bruteForce(block_size, characters):
    flag = ""
    #brute force block comparison
    while True:
        #construct a number of bytes that fits the block size
        plaintext_bytes = b'3' * (block_size - len(flag))
        ciphertext1 = encrypt(plaintext_bytes)
        for char in characters:
            ciphertext2 = encrypt(plaintext_bytes + flag.encode() + char.encode())
            #compare brute force with actual flag
            if ciphertext1[32:64] == ciphertext2[32:64]:
                flag += char
                print(char)
                break
              

        if flag[-1] == '}':
            return flag
        
    
print(bruteForce(block_size, characters))