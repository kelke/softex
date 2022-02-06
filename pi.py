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
        while True:
            prod = base * (base +1) * (base +2)
            if switch:
                pi += d(4) / d(prod)
            else:
                pi -= d(4) / d(prod)
            switch = not switch
            base += 2
            if i >= 1000:
                sim = compare_string_to_file(str(pi),"pi.txt")
                sim -= 2
                print(f"pi accuracy currently at: {sim}")

    except KeyboardInterrupt:
        print("Stopped")
        return pi



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

def calcpi_switch(loop:int, precision: int, lastsim: int, incrloops: Boolean):
    '''
        Increase pi precison by alternating between increasing decimal precision
        and increasing amount of loops
    '''
    start = time.time()

    gc().prec = precision
    pi = nilakantha(loop)

    end = time.time()
    pi = str(pi)
    runtime = end - start
    sim = compare_string_to_file(pi,"pi.txt")

    if sim == lastsim:
        incrloops = not incrloops
    if sim > lastsim:
        s = f"Increased similarity to: {sim} by raising: "
        if incrloops:
            s += "Loops"
        else:
            s += "Precision"
        print(s)
    elif sim < lastsim:
        raise ValueError('Similarity is not supposed to lower')
    if incrloops:
        loop = loop * 1.5
        loop = int(loop)
    else:
        precision = precision * 1.1
        precision = int(precision)
    return pi, sim, runtime
    
def calcpi_loop(loop:int):
    start = time.time()
    pi = nilakantha(loop)
    end = time.time()
    pi = str(pi)
    runtime = end - start
    sim = compare_string_to_file(pi,"pi.txt")
    return pi, sim, runtime

if __name__ == '__main__':
    #gc().prec = 20000
    #loop = int(input("Input number of calculations: "))
    #loop = 800000  #for runtime testing amount of loops stay same

    precision = 500
    gc().prec = precision
    loop = 100
    lastsim = 0
    no_increase_rounds = 0

    incrloops = True # True increases loop amount, False increases precision
    try:
        while True:
            pi, sim, runtime = calcpi_loop(loop)
            loop = int(loop * 1.2)
            if sim > lastsim:
                no_increase_rounds = 0
                print(f"Similartiy now at: {sim}")
            elif sim == lastsim:
                no_increase_rounds += 1
            if no_increase_rounds >= 2:
                print(f"Similarity not increasing after increasing loop amoint")
                precision = int(precision * 1.1)
            lastsim = sim
            
    except KeyboardInterrupt:
        print("Stopped")
        pass


    print(f"Similarity: {sim}")
    print(f"Loops: {loop}")
    print(f"Precision: {precision}")
    # pi = str(pi)
    # write_to_file(pi)

    #print(str(pi)[:100])
    #print(f"Runtime: {end - start}")
    # similarity = compare_string_to_file(str(pi),"pi.txt")
    # print(similarity)