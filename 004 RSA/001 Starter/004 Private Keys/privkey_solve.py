p = 857504083339712752489993810777
q = 1029224947942998075080348647219 
N = p * q
print(f"N: {N}")

phi_N = (p-1) * (q-1)
print(f"Phi of N: {phi_N})")

exponent = 65537
mod_inv = pow(exponent, -1, phi_N)

print(f"Decryption key: {mod_inv}")
