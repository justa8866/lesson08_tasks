# Lekcja 08 — Zadanie 15: Applicator

liczby = list(range(1, 11))

def applicator(func, iterable):
    return [func(x) for x in iterable]

def sqrt(x):
    return x ** 0.5

for nazwa, funkcja in [("kwadraty", lambda x: x ** 2), ("razy 10", lambda x: x * 10), ("pierwiastki", sqrt)]:
    wynik = applicator(funkcja, liczby)
    print(nazwa, wynik)
    assert wynik == list(map(funkcja, liczby))
print("Wyniki zgodne z map().")
