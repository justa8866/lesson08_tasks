# Lekcja 08 — Zadanie 14: Detekcja outlierów IQR

czasy_odpowiedzi = [120, 135, 142, 128, 5000, 138, 145, 119, 10000, 133, 141]

def wykryj_outliery(dane):
    uporzadkowane = sorted(dane)
    n = len(uporzadkowane)
    q1, q3 = uporzadkowane[n // 4], uporzadkowane[3 * n // 4]
    iqr = q3 - q1
    dolna, gorna = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    czyste = [x for x in dane if dolna <= x <= gorna]
    odstajace = [x for x in dane if x < dolna or x > gorna]
    return czyste, odstajace

czyste, outliery = wykryj_outliery(czasy_odpowiedzi)
print("Czyste dane:", czyste)
print("Outliery:", outliery)
