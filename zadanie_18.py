# Lekcja 08 — Zadanie 18: K-fold split

dane = list(range(1, 101))

def k_fold_split(dane, k):
    if k <= 0 or len(dane) % k != 0:
        raise ValueError("k musi być dodatnie i dzielić długość danych")
    rozmiar = len(dane) // k
    return [dane[i * rozmiar:(i + 1) * rozmiar] for i in range(k)]

foldy = k_fold_split(dane, 5)
for nr, fold in enumerate(foldy, 1):
    print(f"Fold {nr} ({len(fold)} elementów): {fold}")
