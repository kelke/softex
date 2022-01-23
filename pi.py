#calculate pi using the Gregory-Leibniz Series
# pi/4 = 1-(1/3)+(1/5)-(1/7)+(1/9)

import decimal as dc

def greglei(x): #amount of terms
    divisor = 3
    pi = dc.Decimal(1)
    loopflag = True
    while loopflag:
        for i in range(x):
            pi -= dc.Decimal(1) / dc.Decimal(divisor)
            divisor += 2
            pi += dc.Decimal(1) / dc.Decimal(divisor)
            divisor += 2
        if input("Repeat? Y/n ") == "n":
            loopflag = False
    pi = pi * dc.Decimal(4)
    return pi


dc.getcontext().prec = 100000
loop = int(input("Input number of calculations: "))
f = open("test.txt", "w")
f.write(str(greglei(loop)))
f.close()