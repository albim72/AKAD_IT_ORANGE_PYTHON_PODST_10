kraj = ["Polska","Norwegia","Kanada","Laos","Egipt","Hiszpania"]

print(kraj)
print(type(kraj))

kraj.append("Turcja")
print(kraj)

kraj.insert(3,"Japonia")
print(kraj)

a = 8
b = 6
v = 89

nb = [a,b,v]
print(nb)

kraj[1] = "Korea"
print(kraj)

kraj[2:4]="Belgia","Szkocja","Chiny","Panama","Meksyk"

print(kraj)

kraj.remove("Chiny")
print(kraj)

hk = kraj.index("Laos")
del kraj[hk]
print(kraj)
kraj.reverse()
print(kraj)
print(len(kraj))

kraj.sort()
print(kraj)

kraj.sort(reverse=True)
print(kraj)

liczby = [23,556,8,-99,112,0,456,13,56,45,9,-99,0,112,45,112,45,112,890]
liczby_arch = liczby.copy()
liczby.sort(reverse=True)
print(liczby)
print(max(liczby))
print(min(liczby))

print(liczby.count(112))
print(liczby[4:9])

print(liczby_arch)

rasa = ["buldog angielski","amstaf","pekińczyk"]
rasa_cena = [7500,6500,4500]


dodatek = [["rodesian","labrador",str(45)],[6000,4000,True]]

#konkatenacja list
rasa = rasa + dodatek[0]
rasa_cena = rasa_cena + dodatek[1]

sklepzoo = [[rasa,"kot","pyton","papuga","szynszyla","szczur"],[rasa_cena,2300,2800,8900,250,70]]

print(sklepzoo[0])
print(sklepzoo[0][1],", cena:",sklepzoo[1][1],"zł")
print(sklepzoo[0][0][0],", cena:",sklepzoo[1][0][0],"zł")

print(rasa)
rasa.sort()
print(rasa)

print(rasa_cena)
rasa_cena.sort()
print(rasa_cena)

rasa_cena = rasa_cena * 3
print(rasa_cena)

litery = ['a','b','c','d','e','f','g','h']

print("litery przed zmianą",litery)

litery[2:7] = [99,102,33]

print("litery po zmianie",litery)

litery_m = litery
litery_p = list(litery)
litery_q = litery[:]

print("litery przed zmianą",litery)
print("litery_m przed zmianą",litery_m)
print("litery_p przed zmianą",litery_p)
print("litery_q przed zmianą",litery_q)

litery [:] = [1002,1003,1114,1116]

print("litery po zmianie",litery)
print("litery_m po zmianie",litery_m)
print("litery_p po zmianie",litery_p)
print("litery_q po zmianie",litery_q)

kolory = ['biały','czerwony','zielony','niebieski','czarny','fioletowy']

#stwórz dwie tablice: parz i nieparz
#do tablicy parz przypisz wszyskie wartości tablicy kolory z indeksami parzystmi
#do tablicy nieparz przypisz wszyskie wartości tablicy kolory z indeksami nieparzystmi
