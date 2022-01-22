import numpy as np
import decimal as de

def split(x, n): # returns a list
    r = divmod(x,1)[1]
    s = str(r)
    for i in range(1,5):
        print("round: "+str(i))

    fir = 1+n
    sec = fir+n
    print(s[2:4])
    #l = []
    return

de.getcontext().prec = 100
rep = de.Decimal(1) / de.Decimal(7)
split(rep, 0)
print(rep)
