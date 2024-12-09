import requests
import json
from pwn import xor 

def encrypt():
    r = requests.get(f"https://aes.cryptohack.org/bean_counter/encrypt/")
    return json.loads(r.text)["encrypted"]

png_header = "89504e470d0a1a0a0000000d49484452"
ciphertext = encrypt()

key = xor(bytes.fromhex(png_header), bytes.fromhex(ciphertext)[:16])
img = xor(bytes.fromhex(ciphertext), key)


flag_png = open("flag.png", 'wb')
flag_png.write(img)