p = 28151

def gen_order(g, p):
    for n in range(2, p):
        if pow(g, n, p) == g:
            return n
    return p
		

#Brute force
for g in range(2, p):
	if (gen_order(g, p)  == p): 
		print(g) 
		break