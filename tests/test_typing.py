import pytest

from py_core.typing_lab import (
    Kullanici,
    KullaniciId,
    Kutu,
    bos_mu,
    esle_generic,
    guvenli_bol,
    id_metni,
    ilk_veya,
    kullanici_ozeti,
    renk_kodu,
    toplam_alan,
)


def test_guvenli_bol():
    assert guvenli_bol(10, 2) == 5.0
    assert guvenli_bol(1, 0) is None


def test_ilk_veya():
    assert ilk_veya([3, 1], 0) == 3
    assert ilk_veya([], 0) == 0
    assert ilk_veya(["a"], "z") == "a"


def test_renk_kodu():
    assert renk_kodu("kirmizi") == "#FF0000"
    with pytest.raises(KeyError):
        renk_kodu("mor")  # type: ignore[arg-type]


def test_kullanici_ozeti():
    k: Kullanici = {"ad": "kumru", "yas": 25, "aktif": True}
    assert kullanici_ozeti(k) == "kumru (25)"


def test_toplam_alan():
    class SahteSekil:
        def __init__(self, a: float) -> None:
            self._a = a

        def alan(self) -> float:
            return self._a

    assert toplam_alan([SahteSekil(2), SahteSekil(3)]) == 5.0


def test_esle_generic():
    assert esle_generic([1, 2, 3], str) == ["1", "2", "3"]
    assert esle_generic(["a", "bb"], len) == [1, 2]


def test_bos_mu():
    assert bos_mu([]) is True
    assert bos_mu("abc") is False
    assert bos_mu({1: 2}) is False


def test_id_metni():
    uid = KullaniciId(7)
    assert id_metni(uid) == "kullanici-7"


def test_kutu():
    k = Kutu(42)
    assert k.ac() == 42
    m = Kutu("merhaba")
    assert m.ac() == "merhaba"


def test_kutu_esle():
    assert Kutu(3).esle(lambda x: x * 2).ac() == 6
