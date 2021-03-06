#calculate pi using the Gregory-Leibniz Series
# pi/4 = 1-(1/3)+(1/5)-(1/7)+(1/9)

from decimal import Decimal as d, getcontext as gc
import time
import random

def write_to_file(content: str) -> None:
    f = open("calculated_pi.txt", "w")
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

def nilakantha(loops: int) -> d():
    '''
        Nilakantha Series = 3 + 4/(2 + 3 + 4) - 4/(4 + 5 + 6) + 4/(6 + 7 + 8) - 4/(8 + 9 + 10)
        using modulo

        i increases +1 per for loop.
        i*2 is the base for (x + y + z)
        every two for loops the 4/(x + y + z) group gets subtracted
    '''
    pi = 3
    base = 2
    switch = True
    
    for i in range (1, (loops+1)*2):
        base = i*2
        prod = base * (base +1) * (base +2)
        if switch:
            pi += d(4) / d(prod)
        else:
            pi -= d(4) / d(prod)
        switch = not switch
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
        stopafter = 500000
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
            loops += stopafter
            print(f"pi accuracy currently at: {sim} | loops: {loops}")

    except KeyboardInterrupt:
        print("Stopped by Keyboard")

    return pi, loops

def montecarlo(loops: int) -> d():
    '''
        imagine circle inside square
        generate random points on square
        count points inside and outside of sqare
    # '''
    circle_points = 0
    for square_points in range(loops):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        if x*x + y*y <= 1:
            circle_points += 1
    square_points += 1
    print(f"Of {square_points} points in the square, {circle_points} were inside the circle")
    pi = d(circle_points)/d(square_points)
    pi = d(4) * d(pi)
    print(pi)
    return pi

def montecarlo_unlim() -> d():
    square_points = 0
    circle_points = 0
    try:
        while True:
            x = random.uniform(-1,1)
            y = random.uniform(-1,1)
            if x*x + y*y <= 1:
                circle_points += 1
            square_points += 1
    except KeyboardInterrupt:
        print("Stopped by Keyboard")
    print(f"Of {square_points} points in the square, {circle_points} were inside the circle")
    pi = d(circle_points) / d(square_points)
    pi = d(4) * d(pi)
    return pi, square_points


if __name__ == '__main__':
    loop = 0
    method = input("Input calculation type(Nilakantha(better) or Monte Carlo): ")
    strloop = input("Input number of calculations(0 runs until Ctrl-C): ")
    try:
        loop = int(strloop)
    except ValueError:
        print("Selected unlimited mode, end with Ctrl-C")
    method = method[0].lower()

    precision = 500
    gc().prec = precision

    start = time.time()
    if method == "n":
        if loop == 0:
            pi, loop = nilakantha_unlim()
        else:
            pi = nilakantha(loop)
    elif method == "m":
        if loop == 0:
            pi, loop = montecarlo_unlim()
        else:
            pi = montecarlo(loop)
    end = time.time()
    runtime = end - start
    runtime = str(runtime)
    pi = str(pi)
    sim = compare_string_to_file(pi, "pi.txt")
    print(f"Accuracy in digits: {sim-2}")
    print(f"Loops: {loop}")
    print(f"Precision: {precision}")
    print(f"Time: {runtime}")
    print(f"Calculated pi: {pi[:sim]}")
    write_to_file(pi[:sim])
    print(f"Calculated pi was written to calculated_pi.txt")