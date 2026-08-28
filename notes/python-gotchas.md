# Python Tuzak Koleksiyonu

Format: kod → tahminim → gerçek → neden → kural.
Hedef: 40 madde.

---

## 1. Mutable default argüman

```python
def ekle(x, liste=[]):
    liste.append(x)
    return liste
```

**Gerçek:** Ardışık çağrılar `[1]`, `[1,2]`, `[1,2,3]` döndürüyor — liste sıfırlanmıyor.
Üçünü tek `print`'te çağırırsam üçü de `[1,2,3]` görünüyor, çünkü **hepsi aynı nesne**.

**Neden:** Varsayılan değer fonksiyon **tanımlandığında bir kez** oluşturulur, her çağrıda değil.

**Kural:** Varsayılan olarak `None` yaz, gövdede oluştur:
```python
def ekle(x, liste=None):
    if liste is None:
        liste = []
```

---

## 2. Liste çarpımı iç nesneyi kopyalamaz

```python
a = [[0] * 3] * 3
a[0][0] = 1   # → [[1,0,0], [1,0,0], [1,0,0]]
```

**Neden:** `* 3` aynı iç listeye **üç referans** üretiyor, üç ayrı liste değil.

**Kural:** `[[0]*3 for _ in range(3)]` — comprehension her turda yeni liste kurar.

---

## 3. `is` vs `==` ve sayı önbelleği

```python
x = 256; y = 256   # x is y → True
p = 257; q = 257   # dosyada True, REPL'de False
```

**Neden:** CPython −5..256 arası tam sayıları önbellekte tutar. 257 önbellek dışında; ama
dosya olarak çalıştırıldığında derleyici aynı kod nesnesindeki eşit sabitleri tekilleştirir.
REPL'de her satır ayrı kod nesnesi olduğu için tekilleştirme olmaz.

**Kural:** Sayı ve string'de **asla `is` kullanma**. `is` sadece `None`, `True`, `False`
ve "gerçekten aynı nesne mi" sorusu için.

---

## 4. `copy` yüzeysel, `deepcopy` derin

```python
s = copy.copy(orj)      # iç listeler PAYLAŞILIR
d = copy.deepcopy(orj)  # iç listeler de kopyalanır
```

**Kural:** İç içe yapı varsa `deepcopy`. Ama pahalıdır — büyük veride önce
"gerçekten kopya mı lazım?" diye sor.

---

## 5. Tuple'ın değişmezliği yüzeyseldir

```python
t = (1, [2, 3])
t[1].append(4)   # → (1, [2, 3, 4])
```

**Neden:** Tuple **kendi elemanlarına olan referansları** dondurur, o nesnelerin içeriğini değil.

**Kural:** Tuple'ı hashlenebilir sanma — içinde liste varsa `dict` anahtarı olamaz.

---

## 6. Parametreye yeniden atama dışarıyı etkilemez

```python
def temizle(liste):
    liste = []      # sadece yerel adı yeniden bağlar
    # liste.clear() olsaydı dışarıyı DEĞİŞTİRİRDİ
```

**Kural:** Python'da "referansla mı değerle mi" sorusunun cevabı burada:
nesneyi **değiştirmek** dışarıya yansır, adı **yeniden bağlamak** yansımaz.

---

## 7. Modül adı stdlib'i gölgeliyor

`collections.py` veya `typing.py` adında bir dosya, stdlib modülünü gölgeler.
`from collections import Counter` senin dosyanı bulmaya çalışır; mypy de bozulur.

**Kural:** Modül adı koymadan önce `python3 -c "import <ad>"` ile stdlib'de var mı bak.

---

## 8. Anahtar kelime modül adı olamaz

`async.py` dosyası oluşturulabilir ama `import py_core.async` **sözdizimi hatası** verir.

**Kural:** `async`, `class`, `import`, `lambda`, `from`, `is`, `not` — hiçbiri modül/değişken adı olamaz.
Liste: `python3 -c "import keyword; print(keyword.kwlist)"`
