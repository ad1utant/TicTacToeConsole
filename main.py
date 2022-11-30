print("Witaj w grze \"Kółko i Krzyżyk\"")
print("Aby rozpocząć wpisz liczbę z planszy")
print("powodzenia")
#rzeczy potrzebne później
import time
lista=["1","2","3","4","5","6","7","8","9"]
licznik100=100
a="7"
b="8"
c="9"
d="4"
e="5"
f="6"
g="1"
h="2"
i="3"
x=0
y=0
def tablica():
    print("___________________")
    print("|     |     |     |")
    print("|  ",a,"  |  ",b,"  |  ",c,"  |",sep="")
    print("|     |     |     |")
    print("|-----------------|")
    print("|     |     |     |")
    print("|  ",d,"  |  ",e,"  |  ",f,"  |",sep="")
    print("|     |     |     |")
    print("|-----------------|")
    print("|     |     |     |")
    print("|  ",g,"  |  ",h,"  |  ",i,"  |",sep="")
    print("|     |     |     |")
    print("|-----------------|")
setka=9
while setka > 0:
    if x == 9:
        c="X"
    elif x == 8:
        b="X"
    elif x == 7:
        a="X"
    elif x == 6:
        f="X"
    elif x == 5:
        e="X"
    elif x == 4:
        d="X"
    elif x == 3:
        i="X"
    elif x == 2:
        h="X"
    elif x == 1:
        g="X"
# skrypt na wygraną
    if a != "7" and b != "8" and c != "9" and d != "4" and e != "5" and f != "6" and g != "1" and h != "2" and i != "3":
        print("REMIS")
        print("program zostanie zamknięty automatycznie za 10 sekund")
        tablica()
    if (a == "X" and b == "X" and c == "X") or (d == "X" and e == "X" and f == "X") or (g == "X" and h == "X" and i == "X"):
        print("Brawo dla Krzyżyka, udało Ci się wygrać")
        print("program zamknie się automatycznie za 10 sekund :D")
        tablica()
        time.sleep(10)
        exit()
    if (a == "X" and d == "X" and g == "X") or (b == "X" and e == "X" and h == "X") or (c == "X" and f == "X" and i == "X"):
        print("Brawo dla Krzyżyka, udało Ci się wygrać")
        print("program zamknie się automatycznie za 10 sekund :D")
        tablica()
        time.sleep(10)
        exit()
    if (a == "X" and e == "X" and i == "X") or (c == "X" and e == "X" and g == "X"):
        print("Brawo dla Krzyżyka, udało Ci się wygrać")
        print("program zamknie się automatycznie za 10 sekund :D")
        tablica()
        time.sleep(10)
        exit()
# skrypt na wygraną
    if (a == "O" and b == "O" and c == "O") or (d == "O" and e == "O" and f == "O") or (
        g == "O" and h == "O" and i == "O"):
        print("Brawo dla Kołka, udało Ci się wygrać")
        print("program zamknie się automatycznie za 10 sekund :D")
        tablica()
        exit()
    if (a == "O" and d == "O" and g == "O") or (b == "O" and e == "O" and h == "O") or (
            c == "O" and f == "O" and i == "O"):
        print("Brawo dla Kołka, udało Ci się wygrać")
        tablica()
        print("program zamknie się automatycznie za 10 sekund :D")
        time.sleep(10)
        exit()
    if (a == "O" and e == "O" and i == "O") or (c == "O" and e == "O" and g == "O"):
        print("Brawo dla Kołka, udało Ci się wygrać")
        print("program zamknie się automatycznie za 10 sekund :D")
        tablica()
        time.sleep(10)
        exit()
    tablica()
    lista.append(x)
    x = int(input())
    while x in lista:
        print("To pole już jest już zajęte :C")
        x = int(input())
    while licznik100>0:
        print("")
        licznik100-=1
    licznik100 = 100

    if x == 9:
        c = "O"
    elif x == 8:
        b = "O"
    elif x == 7:
        a = "O"
    elif x == 6:
        f = "O"
    elif x == 5:
        e = "O"
    elif x == 4:
        d = "O"
    elif x == 3:
        i = "O"
    elif x == 2:
        h = "O"
    elif x == 1:
        g = "O"
    # skrypt na wygraną
    if a != "7" and b != "8" and c != "9" and d != "4" and e != "5" and f != "6" and g != "1" and h != "2" and i != "3":
        print("REMIS")
        print("program zostanie zamknięty automatycznie za 10 sekund")
        tablica()
        exit()
    if (a == "X" and b == "X" and c == "X") or (d == "X" and e == "X" and f == "X") or (g == "X" and h == "X" and i == "X"):
        print("Brawo dla Krzyżyka, udało Ci się wygrać")
        print("program zamknie się automatycznie za 10 sekund :D")
        tablica()
        time.sleep(10)
        exit()
    if (a == "X" and d == "X" and g == "X") or (b == "X" and e == "X" and h == "X") or (c == "X" and f == "X" and i == "X"):
        print("Brawo dla Krzyżyka, udało Ci się wygrać")
        print("program zamknie się automatycznie za 10 sekund :D")
        tablica()
        time.sleep(10)
        exit()
    if (a == "X" and e == "X" and i == "X") or (c == "X" and e == "X" and g == "X"):
        print("Brawo dla Krzyżyka, udało Ci się wygrać")
        print("program zamknie się automatycznie za 10 sekund :D")
        tablica()
        time.sleep(10)
        exit()
    # skrypt na wygraną
    if (a == "O" and b == "O" and c == "O") or (d == "O" and e == "O" and f == "O") or (g == "O" and h == "O" and i == "O"):
        print("Brawo dla Kołka, udało Ci się wygrać")
        print("program zamknie się automatycznie za 10 sekund :D")
        tablica()
        time.sleep(10)
        exit()
    if (a == "O" and d == "O" and g == "O") or (b == "O" and e == "O" and h == "O") or (c == "O" and f == "O" and i == "O"):
        print("Brawo dla Kołka, udało Ci się wygrać")
        print("program zamknie się automatycznie za 10 sekund :D")
        tablica()
        time.sleep(10)
        exit()
    if (a == "O" and e == "O" and i == "O") or (c == "O" and e == "O" and g == "O"):
        print("Brawo dla Kołka, udało Ci się wygrać")
        print("program zamknie się automatycznie za 10 sekund :D")
        tablica()
        time.sleep(10)
        exit()
    tablica()
    lista.append(x)
    x = int(input())
    while x in lista:
        print("To pole już jest już zajęte :C")
        x = int(input())
    while licznik100>0:
        print("")
        licznik100-=1
    licznik100 = 100
    setka -= 1