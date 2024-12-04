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


def ex_gcd (p,q):

    max_multiple = 100

    for u in range(0, max_multiple):
        for v in range(0, max_multiple):
            mul1 = p * u
            mul2 = q * v

            if (gcd(mul1, mul2) != 1):

                if (u > v):
                    return v
                else:
                    return u


print(ex_gcd(26513, 32321))