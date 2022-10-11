class Kolor:

    #stan -> konstruktor klasy
    def __init__(self,id,nazwa):
        self.idkoloru = id
        self.nazwa = nazwa
        self.paleta = "paleta X"


    #zachowanie -> funkcje klasy (metody)
    def print_kolor(self):
        print(f"Kolor {self.nazwa}, id: {self.idkoloru}, paleta: {self.paleta}")


k1 = Kolor(34,"czerwony")
k2 = Kolor(2,"czarny")

k2.paleta = "paleta A"

k1.print_kolor()
k2.print_kolor()
