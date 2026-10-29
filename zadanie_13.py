# Lekcja 08 — Zadanie 13: Pipeline sprzedażowy

sprzedaz = [(1, "elektronika", 45, 12500), (1, "odziez", 78, 4200), (2, "elektronika", 52, 15200), (2, "odziez", 65, 3800), (3, "elektronika", 38, 9800), (3, "odziez", 82, 5100), (4, "elektronika", 61, 18900), (4, "odziez", 71, 4500)]

def tuple_to_dict(r):
    return {"dzien": r[0], "kategoria": r[1], "liczba_transakcji": r[2], "wartosc": r[3]}

def dodaj_srednia_transakcji(r):
    return {**r, "srednia_transakcji": round(r["wartosc"] / r["liczba_transakcji"], 2)}

def agreguj_po_kategorii(dane):
    sumy = {}
    for r in dane:
        kat = r["kategoria"]
        sumy[kat] = sumy.get(kat, 0) + r["wartosc"]
    return sumy

rekordy = [dodaj_srednia_transakcji(tuple_to_dict(r)) for r in sprzedaz]
ranking = sorted(agreguj_po_kategorii(rekordy).items(), key=lambda x: x[1], reverse=True)
for miejsce, (kat, wartosc) in enumerate(ranking, 1):
    print(f"{miejsce}. {kat}: {wartosc} PLN")
