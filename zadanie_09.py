# Lekcja 08 — Zadanie 9: Normalizacja min-max

wynagrodzenia = [3500, 4200, 5800, 7200, 9500, 4800, 6100]

def normalize_minmax(dane):
    mini, maxi = min(dane), max(dane)
    if maxi == mini:
        return [0.0 for _ in dane]
    wynik = []
    for x in dane:
        wynik.append(round((x - mini) / (maxi - mini), 3))
    return wynik

def normalize_minmax_comp(dane):
    mini, maxi = min(dane), max(dane)
    return [round((x - mini) / (maxi - mini), 3) if maxi != mini else 0.0 for x in dane]

print("Pętla:", normalize_minmax(wynagrodzenia))
print("Comprehension:", normalize_minmax_comp(wynagrodzenia))
assert normalize_minmax(wynagrodzenia) == normalize_minmax_comp(wynagrodzenia)
