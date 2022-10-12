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
