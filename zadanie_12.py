# Lekcja 08 — Zadanie 12: Macierz 10x10

macierz = [[i * j for j in range(1, 11)] for i in range(1, 11)]
for wiersz in macierz:
    print(" ".join(f"{x:4d}" for x in wiersz))
