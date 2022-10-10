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


dodatek = [["rodesian","labrador"],[6000,4000]]

#konkatenacja list
rasa = rasa + dodatek[0]
rasa_cena = rasa_cena + dodatek[1]

sklepzoo = [[rasa,"kot","pyton","papuga","szynszyla","szczur"],[rasa_cena,2300,2800,8900,250,70]]

print(sklepzoo[0])
print(sklepzoo[0][1],", cena:",sklepzoo[1][1],"zł")
print(sklepzoo[0][0][0],", cena:",sklepzoo[1][0][0],"zł")






