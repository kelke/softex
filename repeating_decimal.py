import decimal as de

def split(x, n, s):     # returns a list of possibe repeat numbers.
    #x is input number  example: 0.181818
    #n is repeat length example: 2 = 0. 18 18 18
    #s is start-digit   example: 2 = 0.1 81 81 81
    groups = 2      # how many times to check repeat number within input number
    s += 1          # first digit after fraction is r[2]

    i, r = divmod(x,1)
    sr = str(r)         # string r
    if(r == 0):
        return False
    pointers = [s]
    for i in range(1,groups+1):
        pointers.append(s+n*i)
    #print("Pointers: +str(pointers))

    ol = []
    for i in range(groups):
        ol.append(sr[pointers[i]:pointers[i+1]])
    #print("Possible repeat outputs"+ol)
    return ol

de.getcontext().prec = 100
dividend = int(input("Please enter Dividend: "))
divisor = int(input("Please enter Divisor: "))

rep = de.Decimal(dividend) / de.Decimal(divisor)
pr = split(rep, 2, 2)
print(pr)

if isinstance(dividend, int) and isinstance(divisor, int) and False:
    rep = de.Decimal(dividend) / de.Decimal(divisor)
    print("Input number: "+str(rep))

    found = False
    #for startdigit in range
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
#if not found:
print("No repeat found")