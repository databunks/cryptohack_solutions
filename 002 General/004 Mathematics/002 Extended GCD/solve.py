a = 32321
b = 26513

rem1 = a
rem2 = b

x1 = 1
x2 = 0

y1 = 0
y2 = 1

while rem2 > 0:
    quot,rem = divmod(rem1,rem2)  
    rem1 = rem2
    rem2 = rem
    
    # Beizout identity
    x1,x2 = x2,x1 - quot * x2
    y1,y2 = y2,y1 - quot * y2

print("u: " + str(x1))
print("v: " + str(y1))