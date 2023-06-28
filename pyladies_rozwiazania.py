# 01 Tryb
print("Uczę się")
print("Pythona! :)")
# 02 Tekst
print("count przyjmujstringu:".count("na"))
len("Kamila")
print(len([1,2]))
print(len("Kamila Kazimierska"))
# QA: Jaka jest różnica między metodą a funkcją?
class Person:
    def __init__(self, name):
        self.name = name
    def przedstaw_sie(self):
        return f"Jestem {self.name}"

person = Person("Kamila")
print(person.przedstaw_sie())

def przedstaw_sie(name):
    return f"Jestem {name}"

print(przedstaw_sie("Kamila"))
# QA: Czy mogę mieć własne metody na istniejących obiektach?
class StrPaulina(str):
    def __init__(self, name):
        self.name = name
    def str_pauliny(self):
        return f"string z nazwa {self.name}"

str_p = StrPaulina("some")
print(str_p.replace("s", "S"))
print(str_p.str_pauliny())


# 04 Liczby i funckje
# Napisz funkcję, która zsumuje trzy liczby.
def sum(dzien, miesiac, rok):
    return dzien + miesiac + rok
print(sum(28,6,2023))

# QA: Czy zmienna w funkcji jest widoczna poza funkcją?
# QA: Czy mogę argument funkcji zmienić globalnie przez działanie funkcji?
def change_name(imie):
    return "Jakub"

def get_name(imie, nazwisko):
    imie = change_name(imie)
    imie_nazwisko = imie + " " + nazwisko
    return imie_nazwisko.title()

# 06 Zmienne i funkcje
imie_nazwisko_otrzymane = get_name(imie = "kamil", nazwisko= "synoradzki")
print(imie_nazwisko_otrzymane)

new_name = change_name("Kamil")
print(new_name)

# 07 Listy
lista_uczestnikow = ['Kamil']

def zaaktualizuj_liste_uczestnikow(ls, imie):
    ls.append(imie)
    return ls

zaaktualizuj_liste_uczestnikow(lista_uczestnikow, "Dorota")


print(lista_uczestnikow)

# 10 For
uczestnicy = ["Dorota", "Kamil", "Karolina", "Magda", "Paulina"]
lista_uczestnikow = []
for uczestnik in uczestnicy:
    zaaktualizuj_liste_uczestnikow(lista_uczestnikow, uczestnik)
    # lista_uczestnikow.append(uczestnik)
print(lista_uczestnikow)

