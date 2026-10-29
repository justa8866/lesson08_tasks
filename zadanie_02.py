# Lekcja 08 — Zadanie 2: Konwerter jednostek

def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def celsius_to_kelvin(c):
    return c + 273.15

print(f"{'°C':>8} {'°F':>8} {'K':>8}")
for c in [0, 10, 20, 30, 37, 100]:
    f = celsius_to_fahrenheit(c)
    print(f"{c:8.1f} {f:8.1f} {celsius_to_kelvin(c):8.2f}")
    assert abs(fahrenheit_to_celsius(f) - c) < 1e-9
