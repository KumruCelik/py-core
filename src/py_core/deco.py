import time
from collections.abc import Callable, Iterator
from contextlib import contextmanager
from functools import wraps
from typing import Any


def sayac(f: Callable[..., Any]) -> Callable[..., Any]:
    """Fonksiyonun kaç kez çağrıldığını .cagri_sayisi alanında tutar."""

    @wraps(f)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        wrapper.cagri_sayisi += 1  # type: ignore[attr-defined]
        return f(*args, **kwargs)

    wrapper.cagri_sayisi = 0  # type: ignore[attr-defined]
    return wrapper


def tekrarla(n: int) -> Callable[..., Any]:
    """Fonksiyonu n kez çalıştırır, sonuçları liste olarak döndürür."""

    def decorator(f: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(f)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            return [f(*args, **kwargs) for _ in range(n)]

        return wrapper

    return decorator


def yakala(varsayilan: Any) -> Callable[..., Any]:
    """Fonksiyon hata fırlatırsa varsayılan değeri döndürür."""

    def decorator(f: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(f)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                return f(*args, **kwargs)
            except Exception:
                return varsayilan

        return wrapper

    return decorator


def onbellek(f: Callable[..., Any]) -> Callable[..., Any]:
    """Aynı argümanlarla ikinci çağrıda sonucu önbellekten verir."""
    bellek: dict[tuple[Any, ...], Any] = {}

    @wraps(f)
    def wrapper(*args: Any) -> Any:
        if args not in bellek:
            bellek[args] = f(*args)
        return bellek[args]

    return wrapper


def dogrula_pozitif(f: Callable[..., Any]) -> Callable[..., Any]:
    """Tüm konumsal argümanların pozitif olmasını zorunlu kılar."""

    @wraps(f)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if any(x <= 0 for x in args):
            raise ValueError("Tum konumsal argumanlar pozitif olmali")
        return f(*args, **kwargs)

    return wrapper


def loglu(kayit: list[str]) -> Callable[..., Any]:
    """Her çağrıda fonksiyon adını verilen listeye ekler."""

    def decorator(f: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(f)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            kayit.append(f.__name__)
            return f(*args, **kwargs)

        return wrapper

    return decorator


@contextmanager
def gecici_deger(nesne: Any, alan: str, yeni: Any) -> Iterator[None]:
    """Blok boyunca alanı geçici olarak değiştirir, çıkışta geri alır."""
    eski = getattr(nesne, alan)
    setattr(nesne, alan, yeni)
    try:
        yield
    finally:
        setattr(nesne, alan, eski)


@contextmanager
def yoksay(*hatalar: type[BaseException]) -> Iterator[None]:
    """Belirtilen hata türlerini yutar, diğerlerini geçirir.

    contextlib.suppress'in elle yazılmış hali; egzersiz gereği hazır
    çözüm kullanılmıyor.
    """
    try:  # noqa: SIM105
        yield
    except hatalar:
        pass


@contextmanager
def zaman_olc(kayit: list[float]) -> Iterator[None]:
    """Blok süresini saniye cinsinden verilen listeye ekler."""
    baslangic = time.perf_counter()
    try:
        yield
    finally:
        kayit.append(time.perf_counter() - baslangic)


class Sayac:
    """Sınıf tabanlı context manager; blok içinde sayaç tutar."""

    def __init__(self) -> None:
        self.toplam = 0
        self.kapandi = False

    def __enter__(self) -> "Sayac":
        return self

    def __exit__(self, *args: Any) -> None:
        self.kapandi = True

    def artir(self) -> None:
        self.toplam += 1
