import decimal as de

def split(x, n, s):     # returns a list of possibe repeat numbers.
    #x is input number  example: 0.181818
    #n is repeat length example: 2 = 0. 18 18 18
    #s is start-digit   example: 2 = 0.1 81 81 81
    groups = 3      # how many times to check repeat number within input number
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

def checkrepeat(rep):
    print("Input number: "+str(rep))

    found = False
    for startdigit in range(1,51):
        for groupsize in range (1,51):
            groups = split(rep,groupsize, startdigit)
            if not groups:
                break
            equalgroups = 1
            #print(len(groups))
            for i in range(len(groups)-1):
                if groups[i] == groups[i+1]:
                    equalgroups += 1
            if equalgroups == len(groups):
                found = True
                print("Found repeat at: "+str(startdigit)+" digits after fraction; repeat size: "+str(groupsize))
                s = ""
                for i in range(len(groups)):
                    s += " | "+groups[i]
                print("Repeat number: "+str(rep)[:startdigit+1]+s)
                return rep, startdigit, groupsize
    if not found:
        print("No repeat found")
        return rep, 0, 0

de.getcontext().prec = 200
it_int = False
dividend = ""
divisor = ""
try:
    dividend = int(input("Please enter Dividend: "))
    divisor = int(input("Please enter Divisor: "))
    it_int = True
except ValueError:
    it_int = False


if dividend == "0" and divisor == "0":
    br = 0
    brnumber = 0
    bri = 0
    brj = 0
    for i in range(1,101):
        for j in range(1,101):
            rn = de.Decimal(i) / de.Decimal(j)
            r, s, repeat = checkrepeat(rn)
            if repeat > br:
                br = repeat
                brnumber = r
                bri = i
                brj = j

    print()
    print("biggest repeat number:")
    print("Dividend: "+str(bri))
    print("Divisor: "+str(brj))
    print("Quotient: "+str(brnumber))
    print("with a repeat size of: "+str(br))
elif is_int:
    rep = de.Decimal(dividend) / de.Decimal(divisor)
    checkrepeat(rep)
else:
    print("Bad input, please enter two integers")

