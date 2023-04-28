"""
Mějme zadaný následující seznam naměřených teplot. Seznam obsahuje teploty naměřené pro každý den v týdnu ve čtyřech 
časech - ráno, v poledne, večer a v noci.

teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

a. Vytvoř seznam průměrných teplot pro každý den.
b. Vytvoř seznam ranních teplot.
c. Vytvoř seznam nočních teplot.
d. Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu.
"""
# teploty = [ranni, poledne, vecer, noc]

from statistics import mean
teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

a = [mean(x) for x in teploty]
print(a)

b = [x[0] for x in teploty]
print(b)

c = [x[3] for x in teploty]
print(c)

d = [[x[1], x[3]] for x in teploty]
print(d)