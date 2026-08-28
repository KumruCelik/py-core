import math
from collections import Counter, defaultdict, deque
from typing import NamedTuple


class Nokta(NamedTuple):
    """Düzlemde bir nokta."""

    x: float
    y: float


def en_sik(items: list[str], n: int) -> list[tuple[str, int]]:
    """Frekansa göre en sık geçen n değeri (değer, adet) olarak döndürür."""
    return Counter(items).most_common(n)


def grupla(ciftler: list[tuple[str, str]]) -> dict[str, list[str]]:
    """(anahtar, deger) çiftlerini anahtara göre gruplar."""
    d = defaultdict(list)
    for k, v in ciftler:
        d[k].append(v)
    return dict(d)


def tekrar_edenler(items: list[int]) -> list[int]:
    """Birden fazla kez geçen değerleri artan sırada döndürür."""
    gorulen: set[int] = set()
    tekrar: set[int] = set()
    for x in items:
        if x in gorulen:
            tekrar.add(x)
        else:
            gorulen.add(x)
    return sorted(tekrar)


def ortak_elemanlar(a: list[int], b: list[int]) -> list[int]:
    """İki listede de bulunan değerler, artan sırada."""
    return sorted(set(a) & set(b))


def farki_al(a: list[int], b: list[int]) -> list[int]:
    """a'da olup b'de olmayan değerler, artan sırada."""
    return sorted(set(a) - set(b))


def duzlestir(ic_ice: list[list[int]]) -> list[int]:
    """Bir seviye iç içe listeyi düzleştirir."""
    return [x for alt in ic_ice for x in alt]


def parcala(items: list[int], n: int) -> list[list[int]]:
    """Listeyi n'lik parçalara böler; son parça eksik kalabilir.

    n >= 1 olmalıdır; aksi halde range() ValueError fırlatır.
    """
    return [items[i : i + n] for i in range(0, len(items), n)]


def kayan_pencere(items: list[int], n: int) -> list[tuple[int, ...]]:
    """n uzunluğunda ardışık pencereler üretir.

    n >= 1 varsayılır. n listeden uzunsa boş liste döner.
    """
    return [tuple(items[i : i + n]) for i in range(len(items) - n + 1)]


def son_n(items: list[int], n: int) -> list[int]:
    """Son n elemanı döndürür."""
    return list(deque(items, maxlen=n))


def ters_sozluk(d: dict[str, int]) -> dict[int, str]:
    """Anahtar ve değerleri yer değiştirir.

    Raises:
        ValueError: Aynı değere sahip birden fazla anahtar varsa.
    """
    ters: dict[int, str] = {}
    for k, v in d.items():
        if v in ters:
            raise ValueError(f"Yinelenen deger: {v!r} ({ters[v]!r} ve {k!r})")
        ters[v] = k
    return ters


def sozluk_birlestir(a: dict[str, int], b: dict[str, int]) -> dict[str, int]:
    """İki sözlüğü birleştirir; çakışmada b kazanır."""
    return a | b


def deger_filtrele(d: dict[str, int], esik: int) -> dict[str, int]:
    """Değeri eşikten büyük olan anahtarları tutar."""
    return {k: v for k, v in d.items() if v > esik}


def benzersiz_sirali(items: list[int]) -> list[int]:
    """Tekrarları atar ama ilk görülme sırasını korur."""
    return list(dict.fromkeys(items))


def en_buyuk_deger_anahtari(d: dict[str, int]) -> str | None:
    """En büyük değere sahip anahtar; sözlük boşsa None."""
    if not d:
        return None
    return max(d, key=lambda k: d[k])


def mesafe(p1: Nokta, p2: Nokta) -> float:
    """İki nokta arasındaki Öklid mesafesi."""
    return math.dist(p1, p2)
