imie = "Dorota"
def zamiana_imion_na_nazwiska(lista_imion,lista_nazwisk):
    for a in range(len(lista_imion)):
        lista_imion[a]= lista_imion[a] + " " + lista_nazwisk[a]
    return lista_imion


def wczytaj_do_listy_ze_sciezki(sciezka):
    plik_lista = open(sciezka)
    lista = [linia.replace('\n', '') for linia in plik_lista]
    return lista


# Funkcja, ktora dla argumentu ścieżki listy imion i listy nazwisk,
# zworci liste imion i nazwisk.

def zamien_imiona_na_nazwiska_ze_sciezki(sciezka_imion, sciezka_nazwisk):
    wczytana_lista_imion = wczytaj_do_listy_ze_sciezki(sciezka_imion)
    wczytana_lista_nazwisk = wczytaj_do_listy_ze_sciezki(sciezka_nazwisk)
    nowa_lista = zamiana_imion_na_nazwiska(wczytana_lista_imion, wczytana_lista_nazwisk)
    return nowa_lista

zamien_imiona_na_nazwiska_ze_sciezki("lista_imion.txt", "lista_nazwisk.txt")

