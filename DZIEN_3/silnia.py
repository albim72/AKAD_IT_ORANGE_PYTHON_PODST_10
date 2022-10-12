#n! = 1*2*...n, gdzie n należy N
#double max -> 1.8E+308
#n?? 171

def silnia(n):
    
    if n<0:
        raise ValueError("silnia jest niezdefiniowana dla liczb ujemnych")
    wynik=1
    for i in range(1,n+1):
        wynik *= i
    return wynik

try:
    n = int(input("podaj wartość argumentu n funkcji silnia: "))
    wynik = f"silnia z {n} wynosi: {silnia(n)}"
except ValueError as h:
    print(h)
else:
    print(wynik)
