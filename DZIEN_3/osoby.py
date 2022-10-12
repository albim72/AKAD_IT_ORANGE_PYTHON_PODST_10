class Osoba:
    
    def __init__(self,imie,wiek,waga,wzrost):
        self.imie = imie
        self.wiek = wiek
        self.waga = waga
        self.wzrost = wzrost
        self.info()
        
        
    def info(self):
        print("tworzenie nowej osoby jako obiektu superklasy Osoba...")
        
        
    def print_osoba(self):
        print(f"osoba -> imię: {self.imie}, wiek: {self.wiek} lat(a), waga: {self.waga} kg, wzrost: {self.wzrost} cm.")
        
    
    def wiekza10lat(self):
        return self.wiek + 10
    
    def czypracownik(self):
        return False
