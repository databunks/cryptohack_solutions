import requests
import json

#Mantin, Fluhrer, Shamir attack 
#https://www.youtube.com/watch?v=AHkUCD_EYok


def send_cmd(ciphertext, nonce):
    r = requests.get(f"https://aes.cryptohack.org/oh_snap/send_cmd/{ciphertext}/{nonce}/")
    return json.loads(r.text)

# Algorithm taken from https://github.com/jackieden26/FMS-Attack/blob/master/rc4.py
def swapValueByIndex(box, i, j):
    temp = box[i]
    box[i] = box[j]
    box[j] = temp

# Algorithm taken from https://github.com/jackieden26/FMS-Attack/blob/master/rc4.py
# Initialize S-box.
def initSBox(box):
    if len(box) == 0:
        for i in range(256):
            box.append(i)
    else:
        for i in range(256):
            box[i] = i

# Script modified from https://github.com/jackieden26/FMS-Attack/blob/master/keyRecover.py
box = []
ciphertext = "00"
A = 0
key = [None] * 3

# Keylength = 35: keyLength = int(rows[-1][0]) - 2
for A in range(0, 35):

    prob = [0] * 256

    for k_int in range(0, 256):
        iv = (bytes([A + 3]) + bytes([255]) + bytes([k_int])).hex()
        req = send_cmd(ciphertext, iv)['error']
        keyStream = int.from_bytes(bytes.fromhex(req.split(': ')[1]), byteorder='big')
     
        key[0] = A + 3
        key[1] = 255
        key[2] = k_int

        j = 0
        initSBox(box)

        for i in range(A + 3):
            j = (j + box[i] + key[i]) % 256
            swapValueByIndex(box, i, j)

            # Record the original box[0] and box[1] value.
            if i == 1:
                original0 = box[0]
                original1 = box[1]

        i = A + 3
        z = box[1]

        # if resolved condition is possibly met.
        if z + box[z] == A + 3:
            # If the value of box[0] and box[1] has changed, discard this possibility.
            if (original0 != box[0] or original1 != box[1]):
                continue

            keyByte = (keyStream - j - box[i]) % 256
            prob[keyByte] += 1

        # Assume that the most hit is the correct password.
        higherPossibility = prob.index(max(prob))

    key.append(higherPossibility)
    print(key)

# Get rid of first 24-bit initialization vector.
userInput = bytes(key[3:])
print(userInput)
result = [format(key, 'x') for key in userInput]
rawkey = ''.join(result).upper()
print(rawkey)