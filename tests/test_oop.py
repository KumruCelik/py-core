import dataclasses

import pytest

from py_core.oop import (
    Carpan,
    Daire,
    DonmusNokta,
    Kare,
    Kayit,
    Kitap,
    Kuyruk,
    Para,
    SayiAraligi,
    Sicaklik,
    Vektor,
    Yigin,
)


def test_kitap_dataclass():
    k = Kitap("Kürk Mantolu Madonna", "Sabahattin Ali", 1943)
    assert k.ad == "Kürk Mantolu Madonna"
    assert "1943" in repr(k)
    assert k == Kitap("Kürk Mantolu Madonna", "Sabahattin Ali", 1943)


def test_kitap_sozlukten():
    k = Kitap.sozlukten({"ad": "A", "yazar": "B", "yil": 2000})
    assert k.yil == 2000


def test_kitap_gecerli_yil():
    assert Kitap.gecerli_yil_mi(1943) is True
    assert Kitap.gecerli_yil_mi(-5) is False


def test_donmus_nokta():
    p = DonmusNokta(1.0, 2.0)
    assert p.x == 1.0
    with pytest.raises(dataclasses.FrozenInstanceError):
        p.x = 9.0  # type: ignore[misc]


def test_vektor():
    a = Vektor(1, 2)
    b = Vektor(3, 4)
    assert a + b == Vektor(4, 6)
    assert abs(Vektor(3, 4)) == 5.0
    assert repr(Vektor(1, 2)) == "Vektor(1, 2)"


def test_vektor_hash():
    assert len({Vektor(1, 2), Vektor(1, 2)}) == 1
    assert {Vektor(0, 0): "orijin"}[Vektor(0, 0)] == "orijin"


def test_yigin():
    y = Yigin()
    assert not y
    assert len(y) == 0
    y.ekle(1)
    y.ekle(2)
    assert len(y) == 2
    assert bool(y) is True
    assert y.cikar() == 2
    y.cikar()
    with pytest.raises(IndexError):
        y.cikar()


def test_kuyruk_super():
    k = Kuyruk()
    k.ekle(1)
    k.ekle(2)
    assert k.cikar() == 1  # FIFO
    assert len(k) == 1


def test_sicaklik_property():
    s = Sicaklik(100)
    assert s.fahrenheit == pytest.approx(212.0)
    s.fahrenheit = 32.0
    assert s.celsius == pytest.approx(0.0)
    with pytest.raises(ValueError):
        Sicaklik(-300)


def test_sekil_abc():
    with pytest.raises(TypeError):
        from py_core.oop import Sekil

        Sekil()  # type: ignore[abstract]
    assert Kare(3).alan() == 9
    assert Daire(1).alan() == pytest.approx(3.14159, rel=1e-4)


def test_sayi_araligi_iter():
    assert list(SayiAraligi(1, 4)) == [1, 2, 3]
    assert 2 in SayiAraligi(1, 4)
    assert len(SayiAraligi(1, 4)) == 3


def test_carpan_call():
    iki_kat = Carpan(2)
    assert iki_kat(5) == 10
    assert [iki_kat(x) for x in [1, 2]] == [2, 4]


def test_para_hash_eq():
    a = Para(10, "TRY")
    b = Para(10, "TRY")
    assert a == b
    assert len({a, b}) == 1
    assert sorted([Para(5, "TRY"), Para(1, "TRY")])[0] == Para(1, "TRY")


def test_kayit_slots():
    k = Kayit("kumru", 25)
    assert k.ad == "kumru"
    with pytest.raises(AttributeError):
        k.olmayan_alan = 1  # type: ignore[attr-defined]
