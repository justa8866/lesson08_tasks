# Lekcja 08 — Zadanie 10: Agregacja transakcji

transakcje = [{"produkt": "laptop", "wartosc": 2999}, {"produkt": "mysz", "wartosc": 89}, {"produkt": "laptop", "wartosc": 2999}, {"produkt": "klawiatura", "wartosc": 249}, {"produkt": "mysz", "wartosc": 89}, {"produkt": "mysz", "wartosc": 89}]
sumy = {}
for t in transakcje:
    produkt = t["produkt"]
    sumy[produkt] = sumy.get(produkt, 0) + t["wartosc"]
wynik = {produkt: wartosc for produkt, wartosc in sumy.items()}
print(wynik)
