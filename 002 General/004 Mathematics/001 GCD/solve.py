
def gcd (a,b):

    #Check which is greater
    gcd = None

    if a > b:
        gcd = a
    else:
        gcd = b
    

    while (gcd != 0):

        if (a / gcd % 1 == 0 and b / gcd % 1 == 0):
            return gcd
        
        gcd = gcd - 1

print(gcd(66528, 52920))
        