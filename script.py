import math
from collections import Counter

def heron(a: float, b: float, c: float) -> float:
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Aby stworzyć trójkąt, każdy z jego boków musi być dodatni")
    if a + b <= c or b + c <= a or a + c <= b:
        raise ValueError("Z podanych boków nie da się stworzyć trójkąta")
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def wspolne(x: list[int], y: list[int] ) -> list[int]:
    if not x or not y:
        raise ValueError("Zbiory z których ma być wyciągnięta część wspólna nie mogą być puste")
    return list(set(x).intersection(set(y)))

def wspolneMulti(x: list[int], y: list[int] ) -> list[int]:
    if not x or not y:
        raise ValueError("Zbiory z których ma być wyciągnięta część wspólna nie mogą być puste")
    return list(set(x).intersection(set(y)))

def main():
    print("Pole trojkata ze wzoru Herona:", heron(3.0, 4.0, 5.0))
    print("Część wspólna dwóch list:", wspolne([1, 2, 2, 2, 2, 3, 4, 5, 6], [3, 4, 5, 6, 2, 2, 2, 7, 8, 9]))
    imie = input("Jak masz na imię? ")
    print(f"Cześć, {imie}! Miło Cię poznać.")

if __name__ == "__main__":
    main()