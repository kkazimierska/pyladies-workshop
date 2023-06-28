print("Uczę się")
print("Pythona! :)")
print("count przyjmujstringu:".count("na"))
len("Kamila")
print(len([1,2]))
print(len("Kamila Kazimierska"))

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

class StrPaulina(str):
    def __init__(self, name):
        self.name = name
    def str_pauliny(self):
        return f"string z nazwa {self.name}"

str_p = StrPaulina("some")
print(str_p.replace("s", "S"))
print(str_p.str_pauliny())


# Chapter 4
# funkcja przyjmuje argumenty dzien, miesiac, rok
# zwraca sume tych wartosci
def sum(dzien, miesiac, rok):
    return dzien + miesiac + rok
print(sum(28,6,2023))

def change_name(imie):
    return "Jakub"

def get_name(imie, nazwisko):
    imie = change_name(imie)
    imie_nazwisko = imie + " " + nazwisko
    return imie_nazwisko.title()

imie_nazwisko_otrzymane = get_name(imie = "kamil", nazwisko= "synoradzki")
print(imie_nazwisko_otrzymane)

new_name = change_name("Kamil")
print(new_name)

lista_uczestnikow = ['Kamil']

def zaaktualizuj_liste_uczestnikow(ls, imie):
    ls.append(imie)
    return ls

# zaaktualizuj_liste_uczestnikow(lista_uczestnikow, "Dorota")


print(lista_uczestnikow)


uczestnicy = ["Dorota", "Kamil", "Karolina", "Magda", "Paulina"]
lista_uczestnikow = []
for uczestnik in uczestnicy:
    zaaktualizuj_liste_uczestnikow(lista_uczestnikow, uczestnik)
    # lista_uczestnikow.append(uczestnik)
print(lista_uczestnikow)

