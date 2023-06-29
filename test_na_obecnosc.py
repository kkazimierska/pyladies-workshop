from wczytaj_dane import imie
#  imie == "Dorota"

# Zadanie: Napisz funkcję test_imie_Dorota_jest_zapisane_w_wczytaj_dane.
def test_imie_Dorota_jest_zapisane_w_wczytaj_dane():
    assert imie == "Dorota"

# test_wczytaj_imiona_z_pliku
from wczytaj_dane import wczytaj_do_listy_ze_sciezki

def test_wczytaj_imiona_z_pliku():
    wczytana_lista = wczytaj_do_listy_ze_sciezki("lista_imion.txt")
    assert len(wczytana_lista) == 5