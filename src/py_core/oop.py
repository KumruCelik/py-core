import math
from abc import ABC, abstractmethod
from collections import deque
from collections.abc import Iterator
from dataclasses import dataclass
from typing import Any


@dataclass
class Kitap:
    """Kitap kaydı."""

    ad: str
    yazar: str
    yil: int

    @classmethod
    def sozlukten(cls, d: dict[str, Any]) -> "Kitap":
        """Sözlükten Kitap üretir (alternatif kurucu)."""
        return cls(ad=d["ad"], yazar=d["yazar"], yil=d["yil"])

    @staticmethod
    def gecerli_yil_mi(yil: int) -> bool:
        """Yıl makul bir aralıkta mı."""
        return 0 < yil <= 2100


@dataclass(frozen=True)
class DonmusNokta:
    """Değiştirilemez nokta."""

    x: float
    y: float


class Vektor:
    """İki boyutlu vektör; +, ==, abs() ve repr() destekler."""

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: "Vektor") -> "Vektor":
        return Vektor(self.x + other.x, self.y + other.y)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Vektor) and self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __abs__(self) -> float:
        return math.hypot(self.x, self.y)

    def __repr__(self) -> str:
        return f"Vektor({self.x}, {self.y})"


class Yigin:
    """LIFO yığın; len() ve bool() destekler."""

    def __init__(self) -> None:
        self._data: deque[Any] = deque()

    def ekle(self, x: Any) -> None:
        """Sona eleman ekler."""
        self._data.append(x)

    def cikar(self) -> Any:
        """Son eklenen elemanı çıkarır; yığın boşsa IndexError."""
        return self._data.pop()

    def __len__(self) -> int:
        return len(self._data)

    def __bool__(self) -> bool:
        return bool(self._data)


class Kuyruk(Yigin):
    """FIFO kuyruk; Yigin'dan türer, sadece cikar() davranışı değişir."""

    def cikar(self) -> Any:
        """İlk eklenen elemanı çıkarır; kuyruk boşsa IndexError."""
        return self._data.popleft()


class Sicaklik:
    """Celsius/Fahrenheit dönüşümü yapan property örneği."""

    MUTLAK_SIFIR = -273.15

    def __init__(self, celsius: float) -> None:
        self.celsius = celsius  # setter'ı çağırır, doğrulama devrede

    @property
    def celsius(self) -> float:
        """Celsius cinsinden sıcaklık."""
        return self._celsius

    @celsius.setter
    def celsius(self, deger: float) -> None:
        if deger < self.MUTLAK_SIFIR:
            raise ValueError(f"Sicaklik {self.MUTLAK_SIFIR} altinda olamaz: {deger}")
        self._celsius = deger

    @property
    def fahrenheit(self) -> float:
        """Fahrenheit cinsinden sıcaklık."""
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, deger: float) -> None:
        self.celsius = (deger - 32) * 5 / 9


class Sekil(ABC):
    """Soyut şekil arayüzü."""

    @abstractmethod
    def alan(self) -> float:
        """Şeklin alanı."""


class Kare(Sekil):
    """Kare."""

    def __init__(self, kenar: float) -> None:
        self.kenar = kenar

    def alan(self) -> float:
        """Kenar uzunluğunun karesi."""
        return self.kenar**2


class Daire(Sekil):
    """Daire."""

    def __init__(self, yaricap: float) -> None:
        self.yaricap = yaricap

    def alan(self) -> float:
        """pi * r kare."""
        return math.pi * self.yaricap**2


class SayiAraligi:
    """[bas, son) aralığı; iterable, len() ve in destekler."""

    def __init__(self, bas: int, son: int) -> None:
        self.bas = bas
        self.son = son

    def __iter__(self) -> Iterator[int]:
        yield from range(self.bas, self.son)

    def __len__(self) -> int:
        return max(0, self.son - self.bas)

    def __contains__(self, x: int) -> bool:
        return self.bas <= x < self.son


class Carpan:
    """Çağrılabilir nesne: Carpan(2)(5) == 10."""

    def __init__(self, katsayi: int) -> None:
        self.katsayi = katsayi

    def __call__(self, x: int) -> int:
        return self.katsayi * x


@dataclass(frozen=True, order=True)
class Para:
    """Değer nesnesi; hashlenebilir ve sıralanabilir."""

    tutar: int
    birim: str


@dataclass(slots=True)
class Kayit:
    """slots ile tanımlı kayıt; yeni alan eklenemez."""

    ad: str
    yas: int
