import decimal as de

def split(x, n): # returns a list
    r = divmod(x,1)[1]
    s = str(r)
    groups = 2
    pointers = [2]
    for i in range(1,groups+1):
        pointers.append(2+n*i)
    #print("Pointers: "+str(pointers))

    ol = []
    for i in range(groups):
        ol.append(s[pointers[i]:pointers[i+1]])
    #print(ol)
    return ol

de.getcontext().prec = 100
rep = de.Decimal(1) / de.Decimal(7)

found = False
for groupsize in range (1,11):
    groups = split(rep,groupsize)
    equalgroups = 1
    #print(len(groups))
    for i in range(len(groups)-1):
        if groups[i] == groups[i+1]:
            equalgroups += 1
    if equalgroups == len(groups):
        found = True
        print("Found repeat at following amount of digits: "+str(groupsize))
        print("input number: "+str(rep))
        s = ""
        for i in range(len(groups)):
            s += " | "+groups[i]
        print("repeat number: "+str(rep)[:2]+s)
        break
# print("End")