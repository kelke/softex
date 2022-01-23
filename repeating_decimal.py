import decimal as de

def split(x, n):    # returns a list of possibe repeat numbers. x is input number, n is repeat length
    i, r = divmod(x,1)
    s = str(r)
    if(r == 0):
        return False
    groups = 2      # how many times to check repeat number within input number
    pointers = [2]
    for i in range(1,groups+1):
        pointers.append(2+n*i)
    #print("Pointers: +str(pointers))

    ol = []
    for i in range(groups):
        ol.append(s[pointers[i]:pointers[i+1]])
    #print("Possible repeat outputs"+ol)
    return ol

de.getcontext().prec = 100
dividend = int(input("Please enter Dividend: "))
divisor = int(input("Please enter Divisor: "))

if(isinstance(dividend, int) and isinstance(divisor, int)):
    rep = de.Decimal(dividend) / de.Decimal(divisor)
    print("Input number: "+str(rep))

    found = False
    for groupsize in range (1,11):
        groups = split(rep,groupsize)
        if not groups:
            break
        equalgroups = 1
        #print(len(groups))
        for i in range(len(groups)-1):
            if groups[i] == groups[i+1]:
                equalgroups += 1
        if equalgroups == len(groups):
            found = True
            print("Found repeat at following amount of digits: "+str(groupsize))
            s = ""
            for i in range(len(groups)):
                s += " | "+groups[i]
            print("Repeat number: "+str(rep)[:2]+s)
            break
if not found:
    print("No repeat found")