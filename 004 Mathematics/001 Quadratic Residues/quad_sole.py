from math import *

ints = [14, 6, 11]
p = 29

for i in ints:
	for j in range(1,p):
		if i == (j ** 2) % 29:
			print((j ** 2) % 29) 

for a in range(1,29):
	if (a ** 2) % 29 == 6:
		print(a)