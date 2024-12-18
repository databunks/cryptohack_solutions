import requests
import json
from pwn import xor
import itertools

def get_random_encrypted_string():
    r = requests.get("https://aes.cryptohack.org/stream_consciousness/encrypt/")
    return json.loads(r.text)["ciphertext"]


def get_all_encrypted_strings():
    encrypted_string_list = []
    while True:
        random_encrypted_string = get_random_encrypted_string()
        
        if (random_encrypted_string not in encrypted_string_list):
            encrypted_string_list.append(random_encrypted_string)
            print(random_encrypted_string)

def read_encrypted_strings_from_file():
    encrypted_strings = []
    with open('encrypted_string_list.txt', 'r') as file:
        for line in file:
            encrypted_strings.append(bytes.fromhex(line.strip()))
    return encrypted_strings

# get_all_encrypted_strings()
encrypted_strings = read_encrypted_strings_from_file()
pairs = list(itertools.combinations(encrypted_strings, 2))

# guessing at each step (same key is being reused)
string_to_match = b'crypto{'
string_to_match = b'I shall lose everything'
string_to_match = b"Love, probably"
string_to_match = b'I shall, I\'ll lose everything'
string_to_match = b"Love, probably? They don't know"

for pair in pairs:
    xored = xor(pair[0], pair[1])
    output = xor(string_to_match, xored)
    print(str(output))