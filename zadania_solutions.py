import pandas as pd

# Zadanie 2
def grupuj(lista_slownikow, klucz):
    slownik_list_po_kluczu = {}
    for slownik in lista_slownikow:
        if klucz in slownik.keys():
            nowy_klucz = slownik[klucz]
            if nowy_klucz in slownik_list_po_kluczu.keys():
                slownik_list_po_kluczu[nowy_klucz].append(slownik)
            else:
                slownik_list_po_kluczu[nowy_klucz] = [slownik]
    return slownik_list_po_kluczu

owoce = [
    {'nazwa': 'jabłko', 'kolor': 'czerwony'},
    {'nazwa': 'banan', 'kolor': 'żółty'},
    {'nazwa': 'cytryna', 'kolor': 'żółty'},
    {'nazwa': 'gruszka', 'kolor': 'zielony'},
    {'nazwa': 'truskawka', 'kolor': 'czerwony'}
]
grupy = grupuj(owoce, 'kolor')
for kolor, lista_owocow in grupy.items():
     print(kolor, lista_owocow)


# Zadanie 3

posortowane_liczby = [5, 7, 11, 21, 28, 39]

def delta_compression(WE):
    WY = [WE[0]]
    for i in range(1, len(WE)):
        WY.append(WE[i] - WE[i-1])
    return WY

print(delta_compression(posortowane_liczby))

# Zadanie 4
import datetime

def grupuj_i_licz(lista_krotek):
    slownik_pogrupowany = {}

    for krotka in lista_krotek:

        klucz_slownika = (krotka[0].year, krotka[0].month)

        if slownik_pogrupowany.get(klucz_slownika):
            slownik_pogrupowany[klucz_slownika] +=  krotka[1]
        else:
            slownik_pogrupowany[klucz_slownika] = krotka[1]

    return slownik_pogrupowany


x = grupuj_i_licz([
    (datetime.date(2015, 1, 29), 10),
    (datetime.date(2015, 1, 30), 12),
    (datetime.date(2015, 1, 31), 10),
    (datetime.date(2015, 2, 1), 9),
    (datetime.date(2015, 2, 2), 9)
])
print(x)


def tnij(text, numb = None):
    if numb <= len(text):
        list_a = []
        for letters in text:
            list_a.extend(letters)
            cut_list = list_a[0:numb]
        print(cut_list)
    else:
        print("Number given is higher than the number of letters in sentence")

tnij('monikon', 3)
# Zadanie polega na tym żeby pociąć string na 3 znakowe stringi.
#Twoj wynik ma postac ['m', 'o', 'n'], a oczekiwany jest ['mon', 'iko', 'n'].
def tnij(text, dlugosc):
    return [ text[i:i+dlugosc] for i in range(0, len(text), dlugosc) ]
print(tnij('monikon', 3))