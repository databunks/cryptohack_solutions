#!/usr/bin/env python3
from pwn import * 
import json

HOST = "socket.cryptohack.org"
PORT = 13399

r = remote(HOST, PORT)

def json_recv():
    line = r.readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

def json_encode(msg):
    return json.dumps(msg).encode()


print(r.readline())
token = '00' * 28 #zerologin exploit

request = {
    "option": "reset_password",
    'token': token
}
json_send(request)
response = json_recv()
print(response)

request_json = json_encode(request)

while True:
    # sending payload
    r.sendline(request_json)
    r.recvline()
    req_params = {"option": "authenticate", "password": ""}
    r.sendline(json_encode(req_params))
    res = (r.recvline()).decode()
    print(res)

    # checking response payload
    if "crypto{" in res:
        break

    # resetting connection
    reset_connection = {"option": "reset_connection"}
    r.sendline(json_encode(reset_connection))
    r.recvline()
