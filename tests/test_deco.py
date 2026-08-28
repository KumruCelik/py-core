import pytest

from py_core.deco import (
    Sayac,
    dogrula_pozitif,
    gecici_deger,
    loglu,
    onbellek,
    sayac,
    tekrarla,
    yakala,
    yoksay,
    zaman_olc,
)


def test_sayac():
    @sayac
    def selam() -> str:
        return "merhaba"

    assert selam() == "merhaba"
    assert selam() == "merhaba"
    assert selam.cagri_sayisi == 2


def test_sayac_wraps():
    """functools.wraps olmadan bu test düşer."""

    @sayac
    def selam() -> str:
        """Selamlar."""
        return "merhaba"

    assert selam.__name__ == "selam"
    assert selam.__doc__ == "Selamlar."


def test_tekrarla():
    @tekrarla(3)
    def uret() -> int:
        return 7

    assert uret() == [7, 7, 7]


def test_yakala():
    @yakala(varsayilan=-1)
    def bol(a: int, b: int) -> int:
        return a // b

    assert bol(10, 2) == 5
    assert bol(10, 0) == -1


def test_onbellek():
    cagrilar = []

    @onbellek
    def kare(x: int) -> int:
        cagrilar.append(x)
        return x * x

    assert kare(4) == 16
    assert kare(4) == 16
    assert cagrilar == [4]  # ikinci çağrı önbellekten geldi


def test_dogrula_pozitif():
    @dogrula_pozitif
    def topla(a: int, b: int) -> int:
        return a + b

    assert topla(2, 3) == 5
    with pytest.raises(ValueError):
        topla(2, -1)


def test_loglu():
    kayit: list[str] = []

    @loglu(kayit)
    def selam(ad: str) -> str:
        return f"merhaba {ad}"

    selam("kumru")
    assert kayit == ["selam"]


def test_gecici_deger():
    class Ayar:
        seviye = "INFO"

    with gecici_deger(Ayar, "seviye", "DEBUG"):
        assert Ayar.seviye == "DEBUG"
    assert Ayar.seviye == "INFO"


def test_gecici_deger_hata_olsa_da_geri_alir():
    class Ayar:
        seviye = "INFO"

    with pytest.raises(RuntimeError), gecici_deger(Ayar, "seviye", "DEBUG"):
        raise RuntimeError("patladi")
    assert Ayar.seviye == "INFO"


def test_yoksay():
    with yoksay(ZeroDivisionError):
        _ = 1 / 0  # yutulmalı

    with pytest.raises(ValueError), yoksay(ZeroDivisionError):
        raise ValueError("bu yutulmamali")


def test_zaman_olc():
    kayit: list[float] = []
    with zaman_olc(kayit):
        sum(range(1000))
    assert len(kayit) == 1
    assert kayit[0] >= 0


def test_sayac_sinifi():
    with Sayac() as s:
        s.artir()
        s.artir()
    assert s.toplam == 2
    assert s.kapandi is True
