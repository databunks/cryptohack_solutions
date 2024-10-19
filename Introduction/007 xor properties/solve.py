from Crypto.Util.number import *

KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2andKEY1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KEY2andKEY3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
everythingXored = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

KEY2 = str(hex(int.from_bytes(bytes.fromhex(KEY1)) ^ int.from_bytes(bytes.fromhex(KEY2andKEY1)))).split('x')[1]

KEY3 = str(hex(int.from_bytes(bytes.fromhex(KEY2)) ^ int.from_bytes(bytes.fromhex(KEY2andKEY3)))).split('x')[1]

FLAG = int.from_bytes(bytes.fromhex(KEY1)) ^ int.from_bytes(bytes.fromhex(KEY3)) ^ int.from_bytes(bytes.fromhex(KEY2)) ^ int.from_bytes(bytes.fromhex(everythingXored))

print(long_to_bytes(FLAG))

