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
