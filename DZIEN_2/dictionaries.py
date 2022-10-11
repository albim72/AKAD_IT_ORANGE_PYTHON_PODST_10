#słownik -> struktura asocjacyjna (klucz,wartość) -> klucz:wartość -> klucz:numbers, str

samochod = {
    "marka":"Ford",
    "model":"Mustang",
    "rocznik":1974,
    #"marka":"Ford-USA"
}

print(samochod)

m = samochod["model"]
print(m)
samochod["rocznik"] = 2020

print(samochod)

samochod["poj"] = 4.5

print(samochod)

print(len(samochod))

print(samochod.items())
print(samochod.keys())
print(samochod.values())

print("________________klucze____________________")

for x in samochod:
    print(x)

print("_________________wartości  I___________________")

for y in samochod:
    print(samochod[y])

print("_________________wartości  II___________________")

for y in samochod.values():
    print(y)

print("_________________Items ___________________")

for x,y in samochod.items():
    print(x,":",y)


autokomis = {
    "sam1":{
            "marka":"Ford",
            "model":"Mustang",
            "rocznik":1974,
            },
    "sam2":{
            "marka":"Opel",
            "model":"Vectra",
            "rocznik":2008,
            },
    "sam3":{
            "marka":"Jeep",
            "model":"Cherokee",
            "rocznik":2013,
            }

}

print(autokomis)

print(autokomis["sam2"])
print(autokomis["sam2"]["marka"])
