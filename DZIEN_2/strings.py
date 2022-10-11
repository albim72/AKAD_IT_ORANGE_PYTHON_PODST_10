mecz = "mecz miesiąca:\nKlub sportowy: \"Orły Wisła\" - \tTrener: Jan Kot\nlokalizacja: Janowiec\nvs\n" \
       "Klub sportowy: \"KS Siłacz\" - \tTrener: Adam Nowak\nlokalizacja: Siłacze\n"

print(mecz)


str_ = "       niezykle ważna i Tajna wiadmość;      RT5434556445     ;    i Tajna PrzEsYłKA"

print(str_.upper())
print(str_.lower())
print(str_.strip())
print(str_.replace("Tajna","Utajniona"))
pd = str_.split(";")
print(pd)

for i,w in enumerate(pd):
       pd[i] = w.strip()

print(pd)
print(str_.find("Tajna"))
print(str_.endswith("ka"))
print(str_.endswith("KA"))

d = "pionierzy"
e = "32455"

print(d.isalpha())
print(e.isdigit())
