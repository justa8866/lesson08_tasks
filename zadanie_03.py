# Lekcja 08 — Zadanie 3: Filtr liczb parzystych]

parzyste = [x for x in range(1, 101) if x % 2 == 0]
print("Pierwsze 10:", parzyste[:10])
print("Liczba elementów:", len(parzyste))
