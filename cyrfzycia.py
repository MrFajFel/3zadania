dataurodzin = input("podaj w formacie rr/mm/dd ")
liczba = 0
liczba2 = 0
for i in range(len(dataurodzin)):
    liczba = liczba + int(dataurodzin[i])
print(liczba)

wynik = str(liczba)
for i in range(len(wynik)):
    liczba2 = liczba2 + int(wynik[i])
print(liczba2)




