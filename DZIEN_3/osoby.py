class Osoba:

    def __init__(self,imie,wiek,waga,wzrost):
        self.imie = imie
        self.wiek = wiek
        self.waga = waga
        self.wzrost = wzrost
        self.kolor_oczu = "brązowe"
        self.info()


    def info(self):
        print("tworzenie nowej osoby jako obiektu superklasy Osoba...")


    def print_osoba(self):
        print(f"osoba -> imię: {self.imie}, wiek: {self.wiek} lat(a), waga: {self.waga} kg, "
              f"wzrost: {self.wzrost} cm, kolor oczu: {self.kolor_oczu}.")


    def wiekza10lat(self):
        return self.wiek + 10

    def czypracownik(self):
        return False


os1 = Osoba("Jan",38,89,174)
os1.print_osoba()
print(f"wiek za 10 lat: {os1.wiekza10lat()}")
print(f"czy osoba jest pracownikiem? ({os1.czypracownik()})")

print("________________________________________________________")

os2 = Osoba("Ewa",40,58,169)
os2.kolor_oczu = "niebieskie"
os2.print_osoba()
print(f"wiek za 10 lat: {os2.wiekza10lat()}")
print(f"czy osoba jest pracownikiem? ({os2.czypracownik()})")

print("________________________________________________________")

class Pracownik(Osoba):

    #konstruktor klasy z dziedziczeniem
    def __init__(self,imie,wiek,waga,wzrost,firma,stanowisko,latapracy,wynagrodzenie):
        super().__init__(imie,wiek,waga,wzrost)
        self.firma = firma
        self.stanowisko = stanowisko
        self.latapracy = latapracy
        self.wynagrodzenie = wynagrodzenie

    def print_pracownik(self):
        print(f"dane pracownika -> firma: {self.firma}, stanowisko pracy: {self.stanowisko},"
              f"lata pracy: {self.latapracy}, wynagrodzenie: {self.wynagrodzenie} zł")

    def czypracownik(self):
        return True


p1 = Pracownik("Roman",45,109,175,"ABC","dyrektor",12,10900)
p1.print_osoba()
p1.print_pracownik()
print(f"wiek za 10 lat: {p1.wiekza10lat()}")
print(f"czy osoba jest pracownikiem? ({p1.czypracownik()})")

print("________________________________________________________")




