# py-core

[![CI](https://github.com/KumruCelik/py-core/actions/workflows/ci.yml/badge.svg)](https://github.com/KumruCelik/py-core/actions/workflows/ci.yml)

Bölüm 2 (Python ve yazılım mühendisliği disiplini) egzersiz reposu.
Yedi kategoride 80 küçük fonksiyon, her biri testle doğrulanmış.

## Problem

Python'u "çalışan kod yazabiliyorum" seviyesinden "neden böyle çalıştığını
açıklayabiliyorum" seviyesine taşımak. Tutorial takip etmek yerine, her konuda
küçük ve testli parçalar yazarak dilin davranışını ölçmek.

## Yaklaşım

Her egzersiz için önce test (şartname), sonra kod. Her kategori bir modül:

| Modül | Kategori | Egzersiz |
|---|---|---|
| `text.py` | String işleme | 10 |
| `coll.py` | Koleksiyonlar | 15 |
| `gen.py` | Generator / itertools | 10 |
| `deco.py` | Decorator / context manager | 10 |
| `oop.py` | OOP ve veri modelleri | 15 |
| `typing_lab.py` | Tipler ve Protocol | 10 |
| `async_lab.py` | asyncio | 10 |

Çalışma yöntemi: örneği yaz → **çıktısını tahmin et** → çalıştır → tahmin
yanlışsa [`notes/python-gotchas.md`](notes/python-gotchas.md)'ye ekle.

## Kullanım

```
uv sync --all-extras
uv run pre-commit install
make test
```

Tek kategori üzerinde çalışırken sıkı döngü:

```
uv run pytest tests/test_gen.py -x -q --no-cov
```

## Sonuç

```
90 passed

Name                        Stmts   Miss  Cover
------------------------------------------------
src/py_core/async_lab.py       56      0   100%
src/py_core/coll.py            52      0   100%
src/py_core/deco.py            81      0   100%
src/py_core/gen.py             45      0   100%
src/py_core/main.py             6      0   100%
src/py_core/oop.py            103      0   100%
src/py_core/text.py            34      0   100%
src/py_core/typing_lab.py      41      0   100%
------------------------------------------------
TOTAL                         418      0   100%
```

`ruff check`, `ruff format --check` ve `mypy src` temiz.

Yan çıktı: [`notes/python-gotchas.md`](notes/python-gotchas.md) — 20 madde,
hepsi bu repoyu yazarken gerçekten karşılaşılan davranışlar.

## Neyi yapmadım / Sınırlar

- **Testleri ben tasarlamadım.** Şartnameler bana verildi, ben gövdeleri yazdım.
  Kendi test şartnamemi kurmak bir sonraki ödevin (mini-etl) hedefi.
- `pytest` `fixture`, `conftest.py` ve `monkeypatch` hiç kullanılmadı.
- `hypothesis` ile property-based test yok.
- `mypy` tam `--strict` modda değil; `disallow_untyped_defs` dahil en değerli
  anahtarlar tek tek açıldı, gerekçesi `pyproject.toml`'da.
- Türkçe docstring kullanıldığı için `ruff`'ta `allowed-confusables` ile
  Türkçe harflere izin verildi. Kod uluslararası paylaşıma açılırsa
  docstring'ler İngilizceye çevrilmeli.
- Şablondan (`dev-setup`) kalan `main.py` duruyor; egzersizlerle ilgisi yok
  ama `top_n` fonksiyonu koleksiyon kategorisinin bir ön örneği sayılabilir.
- Egzersizler küçük ve bağımsız; gerçek bir uygulama değil. Amaç dil
  davranışını ölçmek, ürün üretmek değil.
