# Lekcja 08 — Zadanie 16: Rekurencja

def silnia(n):
    if n < 0:
        raise ValueError("n musi być nieujemne")
    return 1 if n == 0 else n * silnia(n - 1)

def fibonacci(n):
    if n < 0:
        raise ValueError("n musi być nieujemne")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("10! =", silnia(10))
print("Fibonacci:", [fibonacci(i) for i in range(15)])
