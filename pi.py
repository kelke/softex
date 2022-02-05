#calculate pi using the Gregory-Leibniz Series
# pi/4 = 1-(1/3)+(1/5)-(1/7)+(1/9)

import decimal
from decimal import Decimal as dc

def greglei(x): #amount of terms
    divisor = 3
    pi = dc(1)
    loopflag = True
    while loopflag:
        for i in range(x):
            pi -= dc(1) / dc(divisor)
            divisor += 2
            pi += dc(1) / dc(divisor)
            divisor += 2
        if input("Repeat? Y/n ") == "n":
            loopflag = False
    pi = pi * dc(4)
    return pi

def nilakantha(repeats: int) -> dc():
    pi = 3

    for base in range (2, repeats*2, 2):
        prod = base * (base +1) * (base +2)
        pi += dc(4) / dc(prod)
        print("base:")
        print(base)
        print("prod:")
        print(prod)
        print("")
    return pi

def write_to_file(content: str) -> None:
    f = open("test.txt", "w")
    f.write(content)
    f.close()

if __name__ == '__main__':
    decimal.getcontext().prec = 1000
    loop = int(input("Input number of calculations: "))
    pi = nilakantha(loop)
    print(pi)
    write_to_file(str(pi))