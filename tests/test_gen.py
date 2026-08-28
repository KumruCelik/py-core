from itertools import islice

from py_core.gen import (
    esle_lazy,
    fibonacci,
    filtrele_lazy,
    gruplandir,
    ilk_n,
    parcala_lazy,
    pencerele,
    sonsuz_sayac,
    tekrarsiz_lazy,
    zincirle,
)


def test_sonsuz_sayac():
    assert list(islice(sonsuz_sayac(5), 4)) == [5, 6, 7, 8]


def test_fibonacci():
    assert list(islice(fibonacci(), 8)) == [0, 1, 1, 2, 3, 5, 8, 13]


def test_parcala_lazy():
    assert [list(p) for p in parcala_lazy([1, 2, 3, 4, 5], 2)] == [[1, 2], [3, 4], [5]]
    assert list(parcala_lazy([], 3)) == []


def test_filtrele_lazy():
    assert list(filtrele_lazy(range(10), lambda x: x % 3 == 0)) == [0, 3, 6, 9]


def test_esle_lazy():
    assert list(esle_lazy([1, 2, 3], lambda x: x * x)) == [1, 4, 9]


def test_zincirle():
    assert list(zincirle([1, 2], [], [3])) == [1, 2, 3]
    assert list(zincirle()) == []


def test_tekrarsiz_lazy():
    assert list(tekrarsiz_lazy([3, 1, 3, 2, 1])) == [3, 1, 2]


def test_gruplandir():
    kelimeler = ["armut", "ayva", "elma", "erik"]
    sonuc = [(k, list(g)) for k, g in gruplandir(kelimeler, lambda s: s[0])]
    assert sonuc == [("a", ["armut", "ayva"]), ("e", ["elma", "erik"])]


def test_pencerele():
    assert list(pencerele([1, 2, 3, 4], 2)) == [(1, 2), (2, 3), (3, 4)]
    assert list(pencerele([1], 2)) == []


def test_ilk_n():
    assert list(ilk_n(sonsuz_sayac(0), 3)) == [0, 1, 2]


def test_tembellik():
    """Generator, sonucu istenene kadar hiçbir şey üretmez."""
    calisti = []

    def izle():
        for i in range(3):
            calisti.append(i)
            yield i

    g = esle_lazy(izle(), lambda x: x)
    assert calisti == []  # henüz hiçbir şey üretilmedi
    next(iter(g))
    assert calisti == [0]  # sadece ilk eleman
