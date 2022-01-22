import decimal as de

def split(x, n): # returns a list
    r = divmod(x,1)[1]
    s = str(r)
    groups = 5
    pointers = [2]
    for i in range(1,groups+1):
        pointers.append(2+n*i)
    print("Pointers: "+str(pointers))

    ol = []
    for i in range(groups):
        ol.append(s[pointers[i]:pointers[i+1]])
    return ol

de.getcontext().prec = 100
rep = de.Decimal(1) / de.Decimal(7)
print(split(rep,4))
