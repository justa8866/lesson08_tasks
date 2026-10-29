# Lekcja 08 — Zadanie 1: Kalkulator statystyk

def statystyki(liczby):
    return sum(liczby), round(sum(liczby) / len(liczby), 2), min(liczby), max(liczby)

oceny = [3.5, 4.0, 5.0, 3.0, 4.5, 5.0, 4.0, 3.5]
suma, srednia, minimum, maksimum = statystyki(oceny)
print(f"Suma: {suma}, średnia: {srednia}, min: {minimum}, max: {maksimum}")
