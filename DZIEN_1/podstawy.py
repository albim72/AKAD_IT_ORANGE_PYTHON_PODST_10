print("pierwsza linia programu")

a = 5

print(a)
print(type(a))

a = 'a'
print(a)
print(type(a))

b:float
b = 7
print(b)
print(type(b))

b = True
print(b)
print(type(b))

p1 = "pora roku: jesień"
p2 = "pora roku: zima"
p3 = 2022

print(p1+", a następnie "+p2+" " +str(p3))

print(p1,", a następnie",p2,p3,sep=" -- ")

y = 11.6

print(8*y)

x = '11.12'
print(14*x)
#komentarz jednoliniowy
#CTRL + / - zakomentowanie/odkomentowanie bloku kodu
#CTRL+D - duplikacja linii - bloku
print(14*float(x))
print(14*eval(x))

opis = 'to jest "jedenstka"'
print(opis)

g1,g2 = 11,10

print(g1)
print(g2)
g3=3
print(g1,g2,g3)
g1,g2,g3 = g2,g1,g3
print(g1,g2,g3)

print(g1+g2,g1-g2,g1*g2,g1/g2,g1%g2,g1**g2)

print(round(15.53))
print(round(15.53,1))
print(pow(3,6))
print(3**6)

import math

print(math.exp(4))


i=1
i+=1 #i=i+1

print(i)

txt = "lajkonik"


print(txt)
print(txt[0])
print(txt[1])
print(txt[2:6])
print(txt[:6])
print(txt[3:])
print(txt[-1])
print(txt[-2])
print(txt[:6:2])
print(txt[::-1])







