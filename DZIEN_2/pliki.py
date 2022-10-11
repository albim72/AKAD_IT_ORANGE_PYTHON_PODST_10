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

