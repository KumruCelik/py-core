from collections import deque
from collections.abc import Callable, Iterable, Iterator
from itertools import chain, groupby, islice


def sonsuz_sayac(baslangic: int) -> Iterator[int]:
    """baslangic'tan itibaren sonsuza kadar sayar."""
    while True:
        yield baslangic
        baslangic += 1


def fibonacci() -> Iterator[int]:
    """0, 1, 1, 2, 3, 5... şeklinde sonsuz Fibonacci dizisi."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def parcala_lazy(items: Iterable[int], n: int) -> Iterator[list[int]]:
    """Akışı n'lik parçalara böler; tümünü belleğe almaz."""
    it = iter(items)
    while True:
        parca = list(islice(it, n))
        if not parca:
            return
        yield parca


def filtrele_lazy(items: Iterable[int], kosul: Callable[[int], bool]) -> Iterator[int]:
    """Koşulu sağlayan elemanları tembel olarak üretir."""
    for x in items:
        if kosul(x):
            yield x


def esle_lazy(items: Iterable[int], f: Callable[[int], int]) -> Iterator[int]:
    """Her elemana f uygular, tembel olarak üretir."""
    for x in items:
        yield f(x)


def zincirle(*iterables: Iterable[int]) -> Iterator[int]:
    """Birden fazla akışı tek akış gibi arka arkaya üretir."""
    yield from chain(*iterables)


def tekrarsiz_lazy(items: Iterable[int]) -> Iterator[int]:
    """Tekrarları atar, ilk görülme sırasını korur, tembel çalışır."""
    gorulen: set[int] = set()
    for x in items:
        if x not in gorulen:
            gorulen.add(x)
            yield x


def gruplandir(
    items: Iterable[str], anahtar: Callable[[str], str]
) -> Iterator[tuple[str, list[str]]]:
    """Ardışık aynı anahtarlı elemanları gruplar (girdi sıralı varsayılır)."""
    for k, g in groupby(items, key=anahtar):
        yield k, list(g)


def pencerele(items: Iterable[int], n: int) -> Iterator[tuple[int, ...]]:
    """n uzunluğunda kayan pencereler üretir; tümünü belleğe almaz."""
    pencere: deque[int] = deque(maxlen=n)
    for x in items:
        pencere.append(x)
        if len(pencere) == n:
            yield tuple(pencere)


def ilk_n(items: Iterable[int], n: int) -> Iterator[int]:
    """Akışın ilk n elemanını üretir; sonsuz akışlarda da çalışır."""
    yield from islice(items, n)
