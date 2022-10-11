#pierwsza funkcja
def witaj():
    print("witaj nowy użytkowniku")
    print("opłać abonament")
    print("zaloguj się")

witaj()
witaj()

for i in range(0,25,3):
    print(f"_________wywołanie nr {i+1}_________")
    witaj()
else:
    print("koniec")

#druga funkcja

def obywatel(nrtelefonu,kraj="Polska"):
    print(f"kraj pochodzenia: {kraj}, telefon: {nrtelefonu}")

obywatel(4534534534,"Japonia")
obywatel(6456546546,"Estonia")
obywatel(3425577677,"Grecja")
obywatel(6897876565,"Brazylia")
obywatel(7567786747)
obywatel(None)


#trzecia funkcja

def gx(n):
    return n**5

f = 100
def policz(a,b,x):
    global f
    f = (a+b)*x + f + gx(b)
    return f

print(policz(3,6,2))
print(f)

#czwarta funkcja

def miasta(miasto3,miasto2="Sosnowiec",miasto1="Kraków"):
    print(f"Miasto tygodnia: {miasto1}, grugie miejsce: {miasto2}, trzecie miejsce: {miasto3}")

miasta("Katowice","Wrocław","Toruń")
miasta("Katowice","Wrocław")
miasta("Katowice")
miasta("Rzeszów",None,"Gdańsk")
miasta("Rzeszów",miasto1="Gdańsk")

print("____________________________________________________________")
#piąta funkcja
def zamki(nr_tygodnia,*zamek,rabat):
    print(f"Ranking tygodnia nr: {nr_tygodnia} --> Zamek tygodnia: {zamek[0]} -> rabat: {rabat} zł, drugie miejsce: {zamek[1]}, trzecie miejsce: {zamek[2]}")

zamki(12,"Malbork","Czersk","Będzin","Ogrodzieniec",rabat=20)
zamki(13,"Janowiec","Czorsztyn","Malbork","Czersk","Będzin","Chojnik","Ogrodzieniec",rabat=5)


