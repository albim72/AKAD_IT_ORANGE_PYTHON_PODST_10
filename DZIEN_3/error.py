try:
    z = 5
    print(x)
except NameError:
    print("x nie został zdefiniowany")
except:
    print("nieokreślony błąd!")
else:
    print(f"wejściowe x = {x}")
finally:
    x = 1
    y = 2*x
    print(f"wynik y: {y}")


print(f"kwadrat y: {y**2}")
