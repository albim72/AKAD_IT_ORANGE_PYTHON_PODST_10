import json

x = '{"tytul":"Hobbit","autor":"J.R.R. Tolkien","liczba_sztuk":230}'
print(x)
print(type(x))

x_dict = json.loads(x)
print(x_dict)
print(type(x_dict))

print(x_dict["tytul"])

sam = {
    "marka":"Opel",
    "model":"Insignia",
    "rok":2018
}

jsonsam = json.dumps(sam,indent=4)
print(jsonsam)

with open("sam.json","w",encoding="utf=8") as f:
    f.write(jsonsam)

#do pliku pracownik dodaj nowego pracownika do źródła json -> jako nowy element listy pracowników

def dodaj_nowego_pracownika(new_data,filename="pracownik.json"):

    with open(filename,"r+",encoding="utf-8") as file:
        file_data = json.load(file)
        file_data["pra_info"].append(new_data)
        file.seek(0)
        json.dump(file_data,file,indent=4)

nowy_pracownik = {
            "imie": "Tekla",
            "nazwisko": "Nowak",
            "stanowisko": "prezes",
            "lata_pracy": 12,
            "email": "prezes@firma.pl"
        }

dodaj_nowego_pracownika(nowy_pracownik)
