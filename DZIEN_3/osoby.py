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

    def bmi(self):
        return self.waga/(self.wzrost/100)**2

    def opis_bmi(self):
        if self.bmi()<18.5:
            return "niedowaga"
        elif self.bmi()<=25:
            return "waga prawidłowa"
        elif self.bmi()<=30:
            return "nadwaga"
        else:
            return "otyłość"




os1 = Osoba("Jan",38,89,174)
os1.print_osoba()
print(f"wiek za 10 lat: {os1.wiekza10lat()}")
print(f"czy osoba jest pracownikiem? ({os1.czypracownik()})")
print(f"wynik bmi = {os1.bmi():.2f}, opis: {os1.opis_bmi()}")

print("________________________________________________________")

os2 = Osoba("Ewa",40,58,169)
os2.kolor_oczu = "niebieskie"
os2.print_osoba()
print(f"wiek za 10 lat: {os2.wiekza10lat()}")
print(f"czy osoba jest pracownikiem? ({os2.czypracownik()})")
print(f"wynik bmi = {os2.bmi():.2f}, opis: {os2.opis_bmi()}")

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

class Sport:

    def __init__(self,dyscyplina,lata_upr,best_wynik):
        self.dyscyplina = dyscyplina
        self.lata_upr = lata_upr
        self.best_wynik = best_wynik

    def infosport(self):
        print(f"Dyscyplina: {self.dyscyplina}, czas uprawiania[lata]: {self.lata_upr}, życiówka: {self.best_wynik}")


class Ekstra:
    pass

class Student(Pracownik,Sport,Ekstra):

    #konstruktor z wielodziedziczeniem
    def __init__(self,imie,wiek,waga,wzrost,id_studenta,wydzial,kierunek,rok_stud,
                 firma="",stanowisko="",latapracy="",wynagrodzenie="",dyscyplina="",lata_upr="",best_wynik=""):
        Pracownik.__init__(self,imie,wiek,waga,wzrost,firma,stanowisko,latapracy,wynagrodzenie)
        Sport.__init__(self,dyscyplina,lata_upr,best_wynik)
        self.id_studenta = id_studenta
        self.wydzial = wydzial
        self.kierunek = kierunek
        self.rok_stud = rok_stud

    def print_student(self):
        print(f"dane studenta (id: {self.id_studenta}, wydział: {self.wydzial}, kierunek: {self.kierunek}, "
              f"rok studiów: {self.rok_stud}")

    def czypracownik(self):
        return self.firma != ""

s1 = Student("Olaf",22,77,178,3454,"Budowlany","konstrukcja mostów",3)
s1.print_osoba()
s1.print_student()
print(f"wiek za 10 lat: {s1.wiekza10lat()}")
print(f"czy osoba jest pracownikiem? ({s1.czypracownik()})")


print("________________________________________________________")


s2 = Student("Olga",23,68,179,63455,"Automatyka, Elektronika i Infroamtyka","Informamtyka",4,
             "XYZ","młodszy programista",1,2600)
s2.print_osoba()
s2.print_student()
print(f"wiek za 10 lat: {s2.wiekza10lat()}")
print(f"czy osoba jest pracownikiem? ({s2.czypracownik()})")

#utwórz nowy obiekt klasy Student (s3) który posiada cechy osoby i studenta, nie jest pracownikiem ale jest sportowcem


print("________________________________________________________")


s3 = Student("Robert",22,83,181,45435,"Nauki Społeczne","Socjologia",3,
             dyscyplina="biegi ultra", lata_upr=5, best_wynik="102km 19h 56m 45s")
s3.print_osoba()
s3.print_student()
s3.infosport()
print(f"wiek za 10 lat: {s3.wiekza10lat()}")
print(f"czy osoba jest pracownikiem? ({s3.czypracownik()})")
print(f"wynik bmi = {s3.bmi():.2f}, opis: {s3.opis_bmi()}")






