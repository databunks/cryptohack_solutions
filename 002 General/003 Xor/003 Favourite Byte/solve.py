hex_data = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
data = bytes.fromhex(hex_data)

for key in range(256):
    decoded = ''.join([chr(b ^ key) for b in data])
    
    if (decoded.startswith('crypto')):
        print(decoded)