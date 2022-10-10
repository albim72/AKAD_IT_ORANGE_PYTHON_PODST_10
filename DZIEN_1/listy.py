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
