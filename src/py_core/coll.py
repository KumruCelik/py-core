import math
from collections import Counter, defaultdict, deque
from typing import NamedTuple


class Nokta(NamedTuple):
    x: float
    y: float


def en_sik(items: list[str], n: int) -> list[tuple[str, int]]:
    return Counter(items).most_common(n)


def grupla(ciftler: list[tuple[str, str]]) -> dict[str, list[str]]:
    d = defaultdict(list)
    for k, v in ciftler:
        d[k].append(v)
    return dict(d)


def tekrar_edenler(items: list[int]) -> list[int]:
    seen = set()
    dup = set()
    for x in items:
        if x in seen:
            dup.add(x)
        else:
            seen.add(x)
    return sorted(dup)


def ortak_elemanlar(a: list[int], b: list[int]) -> list[int]:
    return sorted(set(a) & set(b))


def farki_al(a: list[int], b: list[int]) -> list[int]:
    return sorted(set(a) - set(b))


def duzlestir(ic_ice: list[list[int]]) -> list[int]:
    return [x for sub in ic_ice for x in sub]


def parcala(items: list[int], n: int) -> list[list[int]]:
    return [items[i : i + n] for i in range(0, len(items), n)]


def kayan_pencere(items: list[int], n: int) -> list[tuple[int, ...]]:
    return [tuple(items[i : i + n]) for i in range(len(items) - n + 1)]


def son_n(items: list[int], n: int) -> list[int]:
    return list(deque(items, maxlen=n))


def ters_sozluk(d: dict[str, int]) -> dict[int, str]:
    return {v: k for k, v in d.items()}


def sozluk_birlestir(a: dict[str, int], b: dict[str, int]) -> dict[str, int]:
    return a | b


def deger_filtrele(d: dict[str, int], esik: int) -> dict[str, int]:
    return {k: v for k, v in d.items() if v > esik}


def benzersiz_sirali(items: list[int]) -> list[int]:
    return list(dict.fromkeys(items))


def en_buyuk_deger_anahtari(d: dict[str, int]) -> str | None:
    if not d:
        return None
    return max(d, key=lambda k: d[k])


def mesafe(p1: Nokta, p2: Nokta) -> float:
    return math.hypot(p1.x - p2.x, p1.y - p2.y)
