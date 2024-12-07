import requests
import json

ciphertext = "10c8eb4c0355f0f15acdb946c4f068a564de2d63ca7923c3f5edaa107be05a03eab2483f06c1ea65fcbf43a4571c59a8"

def decrypt_ecb_segment(ecb_segment):
    req = requests.get("http://aes.cryptohack.org/ecbcbcwtf/decrypt/" + ecb_segment)
    return (json.loads(req.text))['plaintext'] 

def xor_hex(hex1, hex2):
    return hex(int(hex1, 16) ^ int(hex2, 16))[2:]



initialization_vector = ciphertext[:32]
segmented_ciphertext = [ciphertext[32:64], ciphertext[64:]]
ecb_segment = []

for i in segmented_ciphertext:
    ecb_segment.append(decrypt_ecb_segment(i))


iv_ecb_xor = bytearray.fromhex(xor_hex(initialization_vector,  ecb_segment[0])).decode()
seg_ecb_xor = bytearray.fromhex(xor_hex(segmented_ciphertext[0],  ecb_segment[1])).decode()

print(iv_ecb_xor + seg_ecb_xor)

