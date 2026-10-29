# Lekcja 08 — Zadanie 20: Własne map i filter

liczby = list(range(1, 11))

def my_map(func, iterable):
    wynik = []
    for element in iterable:
        wynik.append(func(element))
    return wynik

def my_filter(predicate, iterable):
    wynik = []
    for element in iterable:
        if predicate(element):
            wynik.append(element)
    return wynik

podwojone = my_map(lambda x: x * 2, liczby)
parzyste = my_filter(lambda x: x % 2 == 0, podwojone)
standardowe = list(filter(lambda x: x % 2 == 0, map(lambda x: x * 2, liczby)))
print("my_map:", podwojone)
print("my_filter:", parzyste)
print("Wbudowane:", standardowe)
assert parzyste == standardowe
print("Wyniki są zgodne.")
