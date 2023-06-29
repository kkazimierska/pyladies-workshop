from pyladies_rozwiazania import imie_nazwisko_otrzymane
# print(imie_nazwisko_otrzymane)

try:
    waluty =('PLN','USD')
    waluty.remove('PLN')
except AttributeError:
    print("Uwaga! Nie stosuj metody remove na krotce.!")

# Zadanie: :snake: Napisz funkcję, która jako argument przyjmie 
# krotkę i zwraca listę,
# która zawiera dokładnie takie same elementy.

waluty =('PLN','USD')

def tuple_to_list(tuple):
    lista_walut = [waluta for waluta in tuple]
    return lista_walut

print(tuple_to_list(waluty))

# try:
#     liczba = int(input("Podaj liczbe:"))
#     print(f"Twoja liczba to: {liczba}!")
# except ValueError:
#     print("Nie wpisuj liczby innej niż całkowita")

# Zadanie: Napisz obsluge błędu ValueError.

def zwroc_wartosc_pod_kluczem(slownik, klucz):
    try:
        return slownik[klucz]
    except KeyError:
        print("Prosze podac klucz, ktory jest w slowniku!")

slownik = {'drzewo': 'klon', 'budynek': 'kamienica'}
klucz = 'kwiat'
zwrocona_wartosc = zwroc_wartosc_pod_kluczem(slownik, klucz)
print(zwrocona_wartosc)
print(slownik.keys())
print(slownik.values())

# 13 Słownik
for klucz, wartosc in slownik.items():
    print(f"Klucz:{klucz}")
    print(f"Wartosc:{wartosc}")
