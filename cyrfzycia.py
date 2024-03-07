dzien = int(input("Podaj dzien"))
miesiac = input("podaj miesiac: ")
rok = int(input("podaj rok:"))
klucz = {"styczen":1,"luty":2,"marzec":3,"kwiecien":4,"maj":5,"czerwiec":6,"lipiec":7,"sierpien":8,"wrzesien":9,"pazdziernik":10,"listopad":11,"grudzien":12}
miesiacjakoliczba = 0
for klucz,wartosc in klucz.items():
    if miesiac == klucz:
        miesiacjakoliczba = wartosc

wynik = dzien+miesiacjakoliczba+rok
print(wynik)
