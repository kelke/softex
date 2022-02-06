#calculate pi using the Gregory-Leibniz Series
# pi/4 = 1-(1/3)+(1/5)-(1/7)+(1/9)

from decimal import Decimal as d, getcontext as gc
import time
import math
from xmlrpc.client import Boolean
import pandas as pd

def nilakantha(repeats: int) -> d():
    '''
        Nilakantha Series = 3 + 4/(2 + 3 + 4) - 4/(4 + 5 + 6) + 4/(6 + 7 + 8) - 4/(8 + 9 + 10)
        using modulo

        i increases +1 per for loop.
        i*2 is the base for (x + y + z)
        every two for loops the 4/(x + y + z) group gets subtracted
    '''
    pi = 3
    base = 2

    for i in range (1, (repeats+1)*2):
        base = i*2
        prod = base * (base +1) * (base +2)
        if i % 2 == 0:
            pi -= d(4) / d(prod)
        else:
            pi += d(4) / d(prod)
    return pi

def nilakantha_unlim():
    '''
        Nilakantha running until abort
    '''
    pi = 3
    base = 2

    try:
        switch = True
        i = 0
        loops = 0
        stopafter = 100000
        while True:
            for i in range(stopafter):
                prod = base * (base +1) * (base +2)
                if switch:
                    pi += d(4) / d(prod)
                else:
                    pi -= d(4) / d(prod)
                switch = not switch
                base += 2
            sim = compare_string_to_file(str(pi),"pi.txt")
            sim -= 2
            loops += stopafter
            print(f"pi accuracy currently at: {sim} | loops: {loops}")

    except KeyboardInterrupt:
        print("Stopped by Keyboard")

    return pi, loops



def write_to_file(content: str) -> None:
    f = open("test.txt", "w")
    f.write(content)
    f.close()

def compare_string_to_file(string: str, filename: str) -> int:
    f = open(filename, "r")
    file_content = f.read()
    f.close()
    prec = 1
    while string[:prec] == file_content[:prec]:
        prec += 1
    return prec-1

if __name__ == '__main__':
    #gc().prec = 20000
    #loop = int(input("Input number of calculations: "))
    #loop = 800000  #for runtime testing amount of loops stay same

    precision = 500
    gc().prec = precision
    start = time.time()

    #pi = nilakantha(10000000)
    pi, loops = nilakantha_unlim()
    end = time.time()
    pi = str(pi)
    sim = compare_string_to_file(pi, "pi.txt")
    print(f"Similarity: {sim}")
    #print(f"Loops: {loops}")
    print(f"Precision: {precision}")
    print(f"time: {end-start}")
    print(f"calculated pi: {pi[:sim]}")
    write_to_file(pi)
    # pi = str(pi)

    #print(str(pi)[:100])
    #print(f"Runtime: {end - start}")
    # similarity = compare_string_to_file(str(pi),"pi.txt")
    # print(similarity)