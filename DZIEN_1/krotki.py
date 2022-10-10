animal = ("pies","kot","krowa","koń","pies","lis","papuga","zając","pies")

print(animal)
print(type(animal))

for a in animal:
    print(a)

print(animal.index("krowa"))
print(animal.count("pies"))

if "papuga" in animal:
    print("Tak! Papuga to zwierz...")

if "budynek" in animal:
    print("To błąd!")

wynik = "krowa" not in animal
print(wynik)

anim2 = ("pająk","ryba")

animal = animal + anim2
print(animal)

obiekt = "Obiekt56",56,True,0.098,"Kraków",19
mojakrotka = tuple(obiekt)
print(mojakrotka)

#Zmodyfikuj krotkę: usuń wartość 56, wstaw wartość 101 na pozycji 3,
#zamień "Kraków" na "Toruń, wsstaw na końcu wartość False

#zamień krotkę na listę mojalista
#zmodyfikuj
#zamień listę na krotkę mojakrotka

mojalista = list(mojakrotka)
mojalista.remove(56)
mojalista.insert(3,101)
u = mojalista.index("Kraków")
mojalista[u] = "Toruń"
mojalista.append(False)

mojakrotka = tuple(mojalista)
print(mojakrotka)

sam = ("audi","Q7",4.6,2020,19800)
(marka,model,poj,rocznik,przebieg) = sam

print(marka)
print(model)
print(poj)
print(rocznik)
print(przebieg)
