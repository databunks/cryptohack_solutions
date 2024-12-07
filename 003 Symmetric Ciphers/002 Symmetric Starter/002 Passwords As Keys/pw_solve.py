from Crypto.Cipher import AES
import hashlib


def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(password_hash)

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}

    
with open("words") as f:
    words = [w.strip() for w in f.readlines()]
    #brute force list
    for word in words:
        password_hash = hashlib.md5(word.encode()).hexdigest()
        decrypted_hex = decrypt("c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66", password_hash).get("plaintext")
        plaintext = bytes.fromhex(decrypted_hex).decode('latin-1')
        if  (plaintext.startswith('crypto{')):
                print(plaintext)


