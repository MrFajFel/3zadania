user1 = input("podaj 1 wyrazenie: ")
user2 = input("podaj 2 wyrazenie: ")
a = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'r':0,'s':0,'t':0,'u':0,'w':0,'x':0,'y':0,'z':0}
b = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'r':0,'s':0,'t':0,'u':0,'w':0,'x':0,'y':0,'z':0}

if user1 == " " and user2 == " ":
    print("Nie mozna takego wyrazenia")
else:
    for i in range(len(user1)):
        for klucz,wartosc in a.items():
            if user1[i] == klucz:
                a[user1[i]] += 1

    for i in range(len(user2)):
        for klucz,wartosc in b.items():
            if user2[i] == klucz:
                b[user2[i]] += 1

if a == b:
    print("to są Anagramy ")
print(a)
print(b)