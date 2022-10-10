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



