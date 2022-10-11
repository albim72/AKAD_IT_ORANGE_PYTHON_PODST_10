drzewa = {"jodła","buk","dąb","jesion","baobab","jabłoń","drzewo sandałowe"}
print(drzewa)
print(drzewa)
print(drzewa)

print("______________________________")
for d in drzewa:
    print(d)

print("osika" in drzewa)

drzewa.add("osika")
print(drzewa)
drzewa.add("osika")
print(drzewa)

las = ["sosna","świerk","brzoza","grab","olcha","grab","sosna","jabłoń"]
drzewa.update(las)

print(drzewa)

las_set = set(las)
print(las_set)
las_unikat = list(las_set)
print(las_unikat)

drzewa.remove("jodła")
print(drzewa)

drzewa.discard("kasztanowiec")
print(drzewa)

drzewa.discard("olcha")
print(drzewa)

dp = drzewa.pop()
print(dp)

print(drzewa)

flas = frozenset(las)
print(flas)


print(flas.difference(drzewa))

fs = set(flas)
print(fs)
print(type(fs))




