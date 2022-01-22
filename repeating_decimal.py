import numpy as np
import decimal as de

def split(x, n): # returns a list
    r = divmod(x,1)[1]
    s = str(r)
    l = [2, 2+n, 2+n*2]
    print("List l: "+str(l))
    ol = [0,0]

    for i in range(2):
        #print()
        #print(l[i])
        #print(l[i+1])
        #print(ol[i])
        ol[i] = s[l[i]:l[i+1]]
    print(ol)
    print(s[2:4])
    #l = []
    return

de.getcontext().prec = 100
rep = de.Decimal(1) / de.Decimal(7)
split(rep, 4)
print(rep)
