from collections.abc import Callable, Iterable, Sequence
from dataclasses import dataclass
from typing import Literal, NewType, Protocol, TypedDict

Renk = Literal["kirmizi", "yesil", "mavi"]

KullaniciId = NewType("KullaniciId", int)

_RENK_KODLARI: dict[str, str] = {
    "kirmizi": "#FF0000",
    "yesil": "#00FF00",
    "mavi": "#0000FF",
}


class Kullanici(TypedDict):
    """Sözlük şeklindeki kullanıcı kaydı."""

    ad: str
    yas: int
    aktif: bool


class Alanli(Protocol):
    """alan() metodu olan her şey."""

    def alan(self) -> float:
        """Alan değeri."""
        ...


class Uzunluklu(Protocol):
    """len() ile ölçülebilen her şey."""

    def __len__(self) -> int:
        """Eleman sayısı."""
        ...


def guvenli_bol(a: float, b: float) -> float | None:
    """b sıfırsa None döndürür."""
    if b == 0:
        return None
    return a / b


def ilk_veya[T](items: Sequence[T], varsayilan: T) -> T:
    """İlk elemanı, dizi boşsa varsayılanı döndürür."""
    if not items:
        return varsayilan
    return items[0]


def renk_kodu(renk: Renk) -> str:
    """Renk adını hex koda çevirir.

    Raises:
        KeyError: Tanımsız bir renk verilirse.
    """
    return _RENK_KODLARI[renk]


def kullanici_ozeti(k: Kullanici) -> str:
    """'ad (yas)' biçiminde özet üretir."""
    return f"{k['ad']} ({k['yas']})"


def toplam_alan(sekiller: Iterable[Alanli]) -> float:
    """Alanların toplamı; tür değil davranış önemli."""
    return sum(s.alan() for s in sekiller)


def esle_generic[T, U](items: list[T], f: Callable[[T], U]) -> list[U]:
    """Her elemana f uygular; giriş ve çıkış tipleri farklı olabilir."""
    return [f(x) for x in items]


def bos_mu(x: Uzunluklu) -> bool:
    """Uzunluğu sıfır mı."""
    return len(x) == 0


def id_metni(uid: KullaniciId) -> str:
    """'kullanici-<id>' biçiminde metin üretir."""
    return f"kullanici-{uid}"


@dataclass
class Kutu[T]:
    """Tek değer taşıyan genel amaçlı kap."""

    deger: T

    def ac(self) -> T:
        """İçindeki değeri döndürür."""
        return self.deger

    def esle[U](self, f: Callable[[T], U]) -> "Kutu[U]":
        """Değeri dönüştürüp yeni bir Kutu döndürür."""
        return Kutu(f(self.deger))
