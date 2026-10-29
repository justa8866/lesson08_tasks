# Lekcja 08 — Zadanie 6: Funkcja z wartościami domyślnymi

def powitanie(imie, jezyk="polski"):
    if jezyk == "polski":
        return f"Cześć, {imie}!"
    elif jezyk == "angielski":
        return f"Hello, {imie}!"
    elif jezyk == "niemiecki":
        return f"Hallo, {imie}!"
    else:
        return "Nieobsługiwany język"

print(powitanie("Anna"))
print(powitanie("Anna", "angielski"))
print(powitanie("Anna", "niemiecki"))
