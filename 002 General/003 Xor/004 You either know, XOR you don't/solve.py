hex_data = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
data = bytes.fromhex(hex_data)


#first 5 bytes are crypto{

# plaintext[i] ^ x = 0xe
# x = 0x0e ^ plaintext[i]

plaintext = 'crypto{'
key = ''

for i in range(0, len(plaintext)):
    key += chr(int(data[i]) ^ ord(plaintext[i])) 

print(key)


# plaintext[i] ^ y = 0xe
# plaintext[i]  = 0xe ^ y

key += 'y'
plaintext += '1'

for i in range(8, len(data)):
    plaintext += chr(int(data[i]) ^ ord(key[i % 8]))

print(plaintext)






