# Lekcja 08 — Zadanie 17: Generator vs lista

n = 1000
lista = [i ** 2 for i in range(n)]
gen = (i ** 2 for i in range(n))
print("Lista:", type(lista), "pierwsze 5:", lista[:5], "len:", len(lista))
pierwsze = []
for i, wartosc in enumerate(gen):
    if i == 5:
        break
    pierwsze.append(wartosc)
print("Generator:", type(gen), "pierwsze 5:", pierwsze)
print("Generator nie obsługuje len(); produkuje wartości na żądanie.")
print("Lista przechowuje wszystkie wartości od razu.")
