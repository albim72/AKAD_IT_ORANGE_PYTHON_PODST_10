import os

f = open("dane.txt","r",encoding="utf-8")
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
f.close()
print("_______________________________________________")
f = open("dane.txt","r",encoding="utf-8")
print(f.read())
f.close()
print("_______________________________________________")
f = open("dane.txt","r",encoding="utf-8")
for x in f:
    print(x)
f.close()

g = open("message.txt","a",encoding="utf-8")
g.write("to jest pierwsza linia pliku\n")
g.close()

f = open("message.txt","r",encoding="utf-8")
print(f.read())
f.close()

if os.path.exists("message.txt"):
    os.remove("message.txt")
    print("plik został usunięty")
else:
    print("plik nie istnieje!")

print("_______________________________________________")
f = open("c:\\Temp\\result.txt","r",encoding="utf-8")
print(f.read())
f.close()

if os.path.exists("c:\\Temp\\result.txt"):
    os.remove("c:\\Temp\\result.txt")
    print("plik został usunięty")
else:
    print("plik nie istnieje!")
