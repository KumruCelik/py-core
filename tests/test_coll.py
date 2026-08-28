import pytest

from py_core.coll import (
    Nokta,
    benzersiz_sirali,
    deger_filtrele,
    duzlestir,
    en_buyuk_deger_anahtari,
    en_sik,
    farki_al,
    grupla,
    kayan_pencere,
    mesafe,
    ortak_elemanlar,
    parcala,
    son_n,
    sozluk_birlestir,
    tekrar_edenler,
    ters_sozluk,
)


def test_en_sik():
    assert en_sik(["a", "b", "a", "c", "a", "b"], 2) == [("a", 3), ("b", 2)]
    assert en_sik([], 3) == []


def test_grupla():
    ciftler = [("meyve", "elma"), ("sebze", "havuc"), ("meyve", "armut")]
    assert grupla(ciftler) == {"meyve": ["elma", "armut"], "sebze": ["havuc"]}
    assert grupla([]) == {}


def test_tekrar_edenler():
    assert tekrar_edenler([1, 2, 2, 3, 3, 3]) == [2, 3]
    assert tekrar_edenler([1, 2, 3]) == []


def test_ortak_elemanlar():
    assert ortak_elemanlar([1, 2, 3, 4], [3, 4, 5]) == [3, 4]
    assert ortak_elemanlar([1], [2]) == []


def test_farki_al():
    assert farki_al([1, 2, 3], [2]) == [1, 3]
    assert farki_al([], [1]) == []


def test_duzlestir():
    assert duzlestir([[1, 2], [3], [], [4, 5]]) == [1, 2, 3, 4, 5]
    assert duzlestir([]) == []


def test_parcala():
    assert parcala([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    assert parcala([], 3) == []


def test_kayan_pencere():
    assert kayan_pencere([1, 2, 3, 4], 2) == [(1, 2), (2, 3), (3, 4)]
    assert kayan_pencere([1], 2) == []


def test_son_n():
    assert son_n([1, 2, 3, 4, 5], 3) == [3, 4, 5]
    assert son_n([1], 5) == [1]


def test_ters_sozluk():
    assert ters_sozluk({"a": 1, "b": 2}) == {1: "a", 2: "b"}
    assert ters_sozluk({}) == {}


def test_ters_sozluk_cakisma():
    with pytest.raises(ValueError):
        ters_sozluk({"a": 1, "b": 1})


def test_sozluk_birlestir():
    assert sozluk_birlestir({"a": 1, "b": 2}, {"b": 9, "c": 3}) == {"a": 1, "b": 9, "c": 3}


def test_deger_filtrele():
    assert deger_filtrele({"a": 5, "b": 1, "c": 9}, 3) == {"a": 5, "c": 9}
    assert deger_filtrele({}, 1) == {}


def test_benzersiz_sirali():
    assert benzersiz_sirali([3, 1, 3, 2, 1]) == [3, 1, 2]
    assert benzersiz_sirali([]) == []


def test_en_buyuk_deger_anahtari():
    assert en_buyuk_deger_anahtari({"a": 1, "b": 9, "c": 5}) == "b"
    assert en_buyuk_deger_anahtari({}) is None


def test_nokta_ve_mesafe():
    p1 = Nokta(0, 0)
    p2 = Nokta(3, 4)
    assert p1.x == 0 and p2.y == 4
    assert mesafe(p1, p2) == pytest.approx(5.0)
