from wczytaj_dane import zamien_imiona_na_nazwiska_ze_sciezki

def test_zamien_imiona_na_nazwiska_ze_sciezki():
    lista_imion_nazwisk = zamien_imiona_na_nazwiska_ze_sciezki("lista_imion.txt", "lista_nazwisk.txt")
    assert len(lista_imion_nazwisk) == 5
    assert lista_imion_nazwisk == ['Dorota Krygowska', 'Kamil Synoradzki', 'Karolina Kovalsky', 'Magda Irla', 'Paulina Bugajska']

# Zadanie. Napisz test, który wczytuje liste imion z pliku lista_imion.tx i sprawdza czy zawiera imie Paulina.
