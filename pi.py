#calculate pi using the Gregory-Leibniz Series
# pi/4 = 1-(1/3)+(1/5)-(1/7)+(1/9)

import decimal
from decimal import Decimal as dc
import time

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
    '''
        Nilakantha Series = 3 + 4/(2 + 3 + 4) - 4/(4 + 5 + 6) + 4/(6 + 7 + 8) - 4/(8 + 9 + 10)
        using modulo
    '''
    pi = 3
    base = 2

    for i in range (1, repeats+1):
        base = i*2
        prod = base * (base +1) * (base +2)
        if i % 2 == 0:
            pi -= dc(4) / dc(prod)
        else:
            pi += dc(4) / dc(prod)
    return pi

def nilakantha2(repeats: int) -> dc():
    '''
        Nilakantha Series = 3 + 4/(2 + 3 + 4) - 4/(4 + 5 + 6) + 4/(6 + 7 + 8) - 4/(8 + 9 + 10)
        using no modulo
    '''
    pi = 3
    base = 2

    for i in range (repeats):
        prod = base * (base +1) * (base +2)
        pi += dc(4) / dc(prod)
        base += 1
        
        prod = base * (base +1) * (base +2)
        pi -= dc(4) / dc(prod)
        base += 1
    return pi

def write_to_file(content: str) -> None:
    f = open("test.txt", "w")
    f.write(content)
    f.close()

if __name__ == '__main__':
    decimal.getcontext().prec = 1000
    loop = int(input("Input number of calculations: "))

    start = time.time()
    pi = nilakantha2(loop)
    end = time.time()

    print(str(pi)[:100])
    print(f"Runtime: {end - start}")
    #write_to_file(str(pi))