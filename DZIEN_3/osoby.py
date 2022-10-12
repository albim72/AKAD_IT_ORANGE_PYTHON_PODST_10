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
