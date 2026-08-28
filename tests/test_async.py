import asyncio
import time

import pytest

from py_core.async_lab import (
    async_uret,
    bekle_ve_don,
    guvenli_calistir,
    ilk_biteni_al,
    paralel_topla,
    sinirli_calistir,
    sirali_topla,
    tekrar_dene,
    topla_async_gen,
    zaman_asimi,
)


async def test_bekle_ve_don():
    assert await bekle_ve_don("x", 0.01) == "x"


async def test_paralel_hizli_siralidan():
    gecikmeler = [0.05, 0.05, 0.05]

    t0 = time.perf_counter()
    await sirali_topla(gecikmeler)
    sirali = time.perf_counter() - t0

    t0 = time.perf_counter()
    await paralel_topla(gecikmeler)
    paralel = time.perf_counter() - t0

    assert paralel < sirali / 2


async def test_paralel_topla_sonuc():
    assert await paralel_topla([0.01, 0.01]) == [0.01, 0.01]


async def test_sinirli_calistir():
    """Semaphore ile aynı anda en fazla 2 görev çalışmalı."""
    aktif = 0
    en_yuksek = 0

    async def gorev() -> None:
        nonlocal aktif, en_yuksek
        aktif += 1
        en_yuksek = max(en_yuksek, aktif)
        await asyncio.sleep(0.02)
        aktif -= 1

    await sinirli_calistir([gorev for _ in range(6)], limit=2)
    assert en_yuksek <= 2


async def test_zaman_asimi():
    assert await zaman_asimi(bekle_ve_don("hizli", 0.01), 0.5) == "hizli"
    assert await zaman_asimi(bekle_ve_don("yavas", 0.5), 0.02) is None


async def test_tekrar_dene():
    cagri = 0

    async def kararsiz() -> str:
        nonlocal cagri
        cagri += 1
        if cagri < 3:
            raise ConnectionError("gecici hata")
        return "tamam"

    assert await tekrar_dene(kararsiz, deneme=5, gecikme=0.01) == "tamam"
    assert cagri == 3


async def test_tekrar_dene_pes_eder():
    async def hep_bozuk() -> str:
        raise ConnectionError("kalici hata")

    with pytest.raises(ConnectionError):
        await tekrar_dene(hep_bozuk, deneme=3, gecikme=0.01)


async def test_ilk_biteni_al():
    sonuc = await ilk_biteni_al([bekle_ve_don("yavas", 0.2), bekle_ve_don("hizli", 0.01)])
    assert sonuc == "hizli"


async def test_async_uret():
    assert [x async for x in async_uret(3)] == [0, 1, 2]


async def test_topla_async_gen():
    assert await topla_async_gen(async_uret(4)) == 6


async def test_guvenli_calistir():
    async def patlar() -> int:
        raise ValueError("hata")

    assert await guvenli_calistir(patlar(), varsayilan=-1) == -1
    assert await guvenli_calistir(bekle_ve_don(5, 0.01), varsayilan=-1) == 5
