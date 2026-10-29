# Lekcja 08 — Zadanie 19: Pipeline klientów

klienci = [{"id": 1, "wiek": 25, "dochod": 4500, "wydatki": 3200}, {"id": 2, "wiek": 200, "dochod": 7800, "wydatki": 5100}, {"id": 3, "wiek": 45, "dochod": 9200, "wydatki": -500}, {"id": 4, "wiek": 30, "dochod": 6000, "wydatki": 4000}, {"id": 5, "wiek": 50, "dochod": 11000, "wydatki": 6500}, {"id": 6, "wiek": 28, "dochod": 5000, "wydatki": 3500}]

def usun_outliery(klienci):
    return [k for k in klienci if 0 <= k["wiek"] <= 120 and k["wydatki"] >= 0]

def normalizuj_pole(klienci, pole):
    if not klienci:
        return []
    mini = min(k[pole] for k in klienci)
    maxi = max(k[pole] for k in klienci)
    return [{**k, f"{pole}_norm": round((k[pole] - mini) / (maxi - mini), 3) if maxi != mini else 0.0} for k in klienci]

def segmentuj(klienci):
    # Progi przyjęte na potrzeby zadania (nie określono ich w PDF).
    return [{**k, "segment": "niski" if k["dochod"] < 5000 else "sredni" if k["dochod"] <= 10000 else "wysoki"} for k in klienci]

czyste = usun_outliery(klienci)
wynik = segmentuj(normalizuj_pole(normalizuj_pole(czyste, "wiek"), "dochod"))
for klient in sorted(wynik, key=lambda k: k["dochod"]):
    print(klient)
