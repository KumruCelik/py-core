import asyncio
from collections.abc import AsyncIterator, Awaitable, Callable, Sequence
from typing import Any


async def bekle_ve_don[T](deger: T, saniye: float) -> T:
    """saniye kadar bekler, sonra değeri döndürür."""
    await asyncio.sleep(saniye)
    return deger


async def sirali_topla(gecikmeler: Sequence[float]) -> list[float]:
    """Gecikmeleri sırayla bekler (yavaş yol)."""
    sonuc: list[float] = []
    for g in gecikmeler:
        await asyncio.sleep(g)
        sonuc.append(g)
    return sonuc


async def paralel_topla(gecikmeler: Sequence[float]) -> list[float]:
    """Gecikmeleri aynı anda bekler; sonuç sırası girdiyle aynı olur."""

    async def bekle(g: float) -> float:
        await asyncio.sleep(g)
        return g

    return await asyncio.gather(*(bekle(g) for g in gecikmeler))


async def sinirli_calistir(
    gorevler: Sequence[Callable[[], Awaitable[Any]]], limit: int
) -> list[Any]:
    """Aynı anda en fazla `limit` görev çalıştırır."""
    sem = asyncio.Semaphore(limit)

    async def sarmala(f: Callable[[], Awaitable[Any]]) -> Any:
        async with sem:
            return await f()

    return await asyncio.gather(*(sarmala(f) for f in gorevler))


async def zaman_asimi[T](coro: Awaitable[T], saniye: float) -> T | None:
    """Süre dolarsa None döndürür, hata fırlatmaz."""
    try:
        return await asyncio.wait_for(coro, timeout=saniye)
    except TimeoutError:
        return None


async def tekrar_dene[T](f: Callable[[], Awaitable[T]], deneme: int, gecikme: float) -> T:
    """Hata alırsa üstel geri çekilmeyle tekrar dener.

    Son deneme de başarısız olursa hatayı yukarı fırlatır.
    """
    for i in range(deneme):
        try:
            return await f()
        except Exception:
            if i == deneme - 1:
                raise
            await asyncio.sleep(gecikme * 2**i)
    raise RuntimeError("ulasilamaz")  # pragma: no cover


async def ilk_biteni_al[T](coroutines: Sequence[Awaitable[T]]) -> T:
    """İlk tamamlanan sonucu döndürür, kalanları iptal eder."""
    gorevler = [asyncio.ensure_future(c) for c in coroutines]
    biten, bekleyen = await asyncio.wait(gorevler, return_when=asyncio.FIRST_COMPLETED)
    for g in bekleyen:
        g.cancel()
    return next(iter(biten)).result()


async def async_uret(n: int) -> AsyncIterator[int]:
    """0'dan n'e kadar (n hariç) asenkron üretir."""
    for i in range(n):
        yield i
        await asyncio.sleep(0)


async def topla_async_gen(agen: AsyncIterator[int]) -> int:
    """Asenkron üreticideki tüm değerleri toplar."""
    toplam = 0
    async for x in agen:
        toplam += x
    return toplam


async def guvenli_calistir[T](coro: Awaitable[T], varsayilan: T) -> T:
    """Hata olursa varsayılanı döndürür."""
    try:
        return await coro
    except Exception:
        return varsayilan
