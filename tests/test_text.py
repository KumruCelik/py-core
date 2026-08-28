import pytest

from py_core.text import (
    anagram_mi,
    bosluklari_sadelestir,
    en_uzun_kelime,
    kelime_say,
    kirp,
    palindrom_mu,
    sayilari_ayikla,
    snake_to_camel,
    tersine_cevir,
    unlu_say,
)


def test_tersine_cevir():
    assert tersine_cevir("merhaba") == "abahrem"
    assert tersine_cevir("") == ""


def test_palindrom_mu():
    assert palindrom_mu("Ey Edip Adanada pide ye") is True
    assert palindrom_mu("merhaba") is False
    assert palindrom_mu("") is True


def test_kelime_say():
    assert kelime_say("a b a c a") == {"a": 3, "b": 1, "c": 1}
    assert kelime_say("") == {}


def test_unlu_say():
    assert unlu_say("merhaba") == 3
    assert unlu_say("bcd") == 0


def test_bosluklari_sadelestir():
    assert bosluklari_sadelestir("  a   b \t c  ") == "a b c"
    assert bosluklari_sadelestir("   ") == ""


def test_en_uzun_kelime():
    assert en_uzun_kelime("kisa uzunca en") == "uzunca"
    assert en_uzun_kelime("") is None


def test_sayilari_ayikla():
    assert sayilari_ayikla("3 elma 12 armut -5 kiraz") == [3, 12, -5]
    assert sayilari_ayikla("hic sayi yok") == []


def test_kirp():
    assert kirp("merhaba dunya", 8) == "merhaba…"
    assert kirp("kisa", 10) == "kisa"


def test_snake_to_camel():
    assert snake_to_camel("kullanici_adi_bilgisi") == "kullaniciAdiBilgisi"
    assert snake_to_camel("tek") == "tek"


def test_anagram_mi():
    assert anagram_mi("kalem", "melak") is True
    assert anagram_mi("kalem", "kale") is False


@pytest.mark.parametrize("girdi,beklenen", [("aa", True), ("ab", False), ("", True)])
def test_palindrom_parametrize(girdi, beklenen):
    assert palindrom_mu(girdi) is beklenen
