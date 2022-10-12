#n! = 1*2*...n, gdzie n należy N
#double max -> 1.8E+308
#n?? 171

import sys

def silnia(n):

    if n<0:
        raise ValueError("silnia jest niezdefiniowana dla liczb ujemnych")
    wynik=1
    for i in range(1,n+1):
        wynik *= i
    return wynik


def silnia_rek(n):

    if n<0:
        raise ValueError("silnia jest niezdefiniowana dla liczb ujemnych")
    if n==0:
        return 1
    else:
        return n*silnia_rek(n-1)

try:
    sys.setrecursionlimit(10000)
    n = int(input("podaj wartość argumentu n funkcji silnia: "))
    wynik = f"silnia z {n} wynosi: {silnia(n)}"
    wynik_rek = f"silnia rekurencyjna z {n} wynosi: {silnia_rek(n)}"
except ValueError as h:
    print(h)
else:
    print(wynik)
    print(wynik_rek)
