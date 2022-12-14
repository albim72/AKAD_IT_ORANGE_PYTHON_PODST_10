wiek = 39
miasto = "Lublin"
imie = "Olga"
uczelnia = "UMCS"
kierunek = "Prawo"

osoba = "opis osoby - imię: {}, miasto: {}, wiek: {}."

print(osoba.format(imie, miasto, wiek))

osoba = "opis osoby - imię: {0}, wiek: {2}, miasto: {1}."

print(osoba.format(imie, miasto, wiek))

# f - string
student = f"student - uczelnia: {uczelnia}, miasto: {miasto}, kierunek: {kierunek}, imię: {imie}, wiek: {wiek}"
print(student)

idw = "kwota12"
kwota = 78.9875545

formatowanie = '%-30s = %.2f zł' % (idw, kwota)
print(formatowanie)

owoce = [
    ('awokado', 8.99),
    ('banan', 4.88),
    ('mandarynka', 9.02),
    ('malina', 12),
    ('smoczy owoc', 10),
    ('winogrono białe', 13.67)
]

print(list(enumerate(owoce)))

# zbuduj cennik wg wzoru -> #nr: nazwa(max 10 znaków) = 0.00 zł

print("**********cennik owoców**************")
for i, (nazwa, cena) in enumerate(owoce):
    print('#%d: %-16s = %6.2f zł' % (i, nazwa, cena))

print("**********nowy cennik owoców**************")
for i, (nazwa, cena) in enumerate(owoce):
    print('#%d: %-16s = %6.2f zł' % (
        i + 1,
        nazwa.title(),
        round(cena, 1)
    ))

