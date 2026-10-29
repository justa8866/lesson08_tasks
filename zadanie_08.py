# Lekcja 08 — Zadanie 8: Map i filter

liczby = [-5, 3, -2, 8, 0, -1, 7, 4, -9, 6]
dodatnie = filter(lambda x: x > 0, liczby)
wynik = list(map(lambda x: x * 2, dodatnie))
print(wynik)
