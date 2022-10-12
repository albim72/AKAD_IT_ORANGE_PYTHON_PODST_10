import sys

try:
    f=open("waznedane.txt","r",encoding="utf-8")
    s = f.readline()
    i = int(s.strip())
    raise Exception(d=i/0)
except OSError as err:
    print(f"błląd systemowy: {err}")
except ValueError:
    print("nie można przekonwertować danych z formatu str na int")
except Exception as exx:
    print(f"właściwa klasa błędu: {type(exx)}")
    print(exx.args)
    print(exx)
except:
    print(f"nieoczekiwany błąd: {sys.exc_info()[0]}")
