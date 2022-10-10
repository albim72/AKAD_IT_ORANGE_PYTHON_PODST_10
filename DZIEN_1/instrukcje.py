#instrukcja warunkowa
a = 22
b = 22

if a>b:
    print("a jest większe niż b")
elif a==1 and b==1:
    print("szczególny przypadek: a=1 i b=1")
elif a == b:
    print("a=",a,"b=",b)
else:
    print("a jest mniejsze niż b")

nr_dt = 2

match nr_dt:
    case 1: print("poniedziałek")
    case 2: print("wtorek")
    case 3: print("środa")
    case 4: print("czwartek")
    case 5: print("piątek")
    case 6: print("sobota")
    case 7: print("niedziela")


#iteracja
i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1
else:
    print("ostateczna wartość i:",i)

print("ciąg dalszy")

owoce = ["jabłko","banan","malina","kiwi","cytyna"]
print(owoce)
print("___lista owoców____")
for owoc in owoce:
    print(owoc)

print("_________________________________________")

cechy = ["kolorowy","elegancki","kosztowny","brudny","oskurny"]
obiekty = ["budynek","samochód","ogród","płaszcz","przystanek"]

for x in cechy:
    for y in obiekty:
        print(x,y)

