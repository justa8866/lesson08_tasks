# Lekcja 08 — Zadanie 11: Feature engineering

klienci = [{"id": 1, "wiek": 25, "dochod": 4500}, {"id": 2, "wiek": 45, "dochod": 9200}, {"id": 3, "wiek": 32, "dochod": 6800}, {"id": 4, "wiek": 28, "dochod": 5200}, {"id": 5, "wiek": 55, "dochod": 12000}]

def kategoria_wieku(wiek):
    return "mlody" if wiek < 30 else "sredni" if wiek <= 50 else "starszy"

def kategoria_dochodu(dochod):
    return "niski" if dochod < 5000 else "sredni" if dochod <= 10000 else "wysoki"

wynik = [{**k, "kat_wiekowa": kategoria_wieku(k["wiek"]), "kat_dochodu": kategoria_dochodu(k["dochod"])} for k in klienci]
for klient in wynik:
    print(klient)
