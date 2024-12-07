from pwn import * # pip install pwntools
from Crypto.Util.number import *
import json
import codecs
import array

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


for i in range(0, 101):
    received = json_recv()
    encoding = received["type"]
    encoded = received["encoded"]
    decoded = ""

    if encoding == "base64":
        decoded = base64.b64decode(encoded).decode() # wow so encode

    elif encoding == "hex":
        hex_decoded = codecs.getdecoder("hex_codec")
        decoded = bytearray.fromhex(encoded).decode()

    elif encoding == "rot13":
        decoded = codecs.encode(encoded, 'rot_13')

    elif encoding == "bigint":
        decoded = long_to_bytes(int(encoded, 16)).decode('utf-8')

    elif encoding == "utf-8":
        for i in encoded:
            decoded += chr(i)

    to_send = {
        "decoded": decoded
    }
    json_send(to_send)
