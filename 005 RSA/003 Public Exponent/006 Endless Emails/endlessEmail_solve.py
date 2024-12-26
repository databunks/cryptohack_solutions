from itertools import combinations
import requests
from functools import reduce
import operator
import gmpy2
from Crypto.Util import number

# Read from file
def readFromFile():
    file = open("output_0ef6d6343784e59e2f44f61d2d29896f.txt", "r")
    content = file.read()
    file.close()
    lines = content.splitlines()
    return lines

lines = readFromFile()

param = []

#parsing
for i in range(0, len(lines), 5):
    n = int(lines[i].split(' ')[-1])
    e = int(lines[i+1].split(' ')[-1])
    c = int(lines[i+2].split(' ')[-1])
    param.append([n, c])


e = 3
def solve(ns, cs):
    n_prod = reduce(operator.mul, ns)  # n_prod is the product of all ns
    n_prod_i = [n_prod // n for n in ns]     # n_prod_i is the product of all ns except n_i (M/n_i)
    ti = [pow(n_prod_i, -1, num) for n_prod_i, num in zip(n_prod_i, ns)]  # Modular inverse of n_prod_i modulo n_i
    chinese_remainder_solve = sum([c * t * m for c, t, m in zip(cs, ti, n_prod_i)]) % n_prod  # Chinese Remainder Theorem solution
    r, same = gmpy2.iroot(chinese_remainder_solve, e)  # Take the e-th root of chinese_remainder_solve and check if it's exact
    if same:
        return r  # If the e-th root is the same, return it (possible plaintext)


for comb in combinations(param, e):
    nums = [i[0] for i in comb]  # Get the list of nums (moduli)
    combos = [i[1] for i in comb]  # Get the list of combos (ciphertexts)
    rem = solve(nums, combos)        # Solve using the Chinese Remainder Theorem and e-th root

    if rem != None:           # check for result
        print(number.long_to_bytes(rem))  # Convert the result to bytes 
    
