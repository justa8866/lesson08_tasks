# Lekcja 08 — Zadanie 5: Lambda do sortowania
produkty = [("laptop", 2999, 4.5), ("mysz", 89, 4.2), ("klawiatura", 249, 4.8), ("monitor", 899, 4.3)]
print("Cena rosnąco:", sorted(produkty, key=lambda p: p[1]))
print("Ocena malejąco:", sorted(produkty, key=lambda p: p[2], reverse=True))
