import re


def tersine_cevir(s: str) -> str:
    """Metni ters çevirir."""
    return s[::-1]


def palindrom_mu(s: str) -> bool:
    """Büyük/küçük harf ve boşlukları yok sayarak palindrom kontrolü."""
    s = s.lower().replace(" ", "")
    return s == s[::-1]


def kelime_say(s: str) -> dict[str, int]:
    """Kelime frekans sözlüğü döndürür."""
    s = s.lower()
    kelimeler = s.split()
    sonuc: dict[str, int] = {}
    for k in kelimeler:
        sonuc[k] = sonuc.get(k, 0) + 1
    return sonuc


def unlu_say(s: str) -> int:
    """Türkçe ünlü harf sayısını döndürür (aeıioöuü)."""
    unluler = "aeıioöuü"
    return sum(1 for c in s.lower() if c in unluler)


def bosluklari_sadelestir(s: str) -> str:
    """Baştaki/sondaki boşlukları atar, aradakileri tek boşluğa indirir."""
    return " ".join(s.split())


def en_uzun_kelime(s: str) -> str | None:
    """En uzun kelimeyi döndürür; metin boşsa None."""
    kelimeler = s.split()
    if not kelimeler:
        return None
    return max(kelimeler, key=len)


def sayilari_ayikla(s: str) -> list[int]:
    """Metindeki tam sayıları (negatifler dahil) sırayla döndürür."""
    return [int(x) for x in re.findall(r"-?\d+", s)]


def kirp(s: str, n: int) -> str:
    """n karakterden uzunsa kırpar ve sonuna … koyar (toplam uzunluk n)."""
    if len(s) <= n:
        return s
    return s[: n - 1] + "…"


def snake_to_camel(s: str) -> str:
    """snake_case → camelCase."""
    parts = s.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


def anagram_mi(a: str, b: str) -> bool:
    """İki metin birbirinin anagramı mı."""
    return sorted(a.replace(" ", "").lower()) == sorted(b.replace(" ", "").lower())
