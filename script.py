import math
from itertools import chain, combinations
from collections import Counter


def heron(a: float, b: float, c: float) -> float:
    """
    Oblicza pole trójkąta za pomocą wzoru Herona.
    Parameters:
    a (float): długość pierwszego boku
    b (float): długość drugiego boku
    c (float): długość trzeciego boku
    Returns: pole powierzchni trójkąta
    Throws: ValueError jeśli boki nie tworzą poprawnego trójkąta
    """
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Aby stworzyć trójkąt, każdy z jego boków musi być dodatni")
    if a + b <= c or b + c <= a or a + c <= b:
        raise ValueError("Z podanych boków nie da się stworzyć trójkąta")
    s = (a + b + c) / 2.0
    return math.sqrt(s * (s - a) * (s - b) * (s - c))



def wspolne(x: list, y: list) -> list:
    """
     Znajduje część wspólną dwóch list, uwzględniając liczbę wystąpień.
     Parameters:
     x (list): pierwsza lista
     y (list): druga lista
     Returns: lista elementów wspólnych
     Throws: ValueError jeśli jedna z list jest pusta
     """
    if not x or not y:
        raise ValueError("Zbiory, z których ma być wyciągnięta część wspólna, nie mogą być puste")
    cx = Counter(x)
    cy = Counter(y)
    result = []
    for element in cx:
        if element in cy:
            result.extend([element] * min(cx[element], cy[element]))
    return result


def podzbiory(x: set) -> list:
    """
    Generuje wszystkie podzbiory danego zbioru.
    Parameters:
    x (set): zbiór wejściowy
    Returns: lista podzbiorów w formie zbiorów
    Throws: ValueError jeśli zbiór jest pusty
    """
    if not x:
        raise ValueError("Zbiór nie może być pusty")
    # Generowanie wszystkich podzbiorów
    return [set(c) for c in chain.from_iterable(combinations(x, r) for r in range(len(x) + 1))]


def fibonacci_iteracja(n: int) -> list:
    """
    Generuje ciąg Fibonacciego metodą iteracyjną.
    Parameters:
    n (int): liczba elementów ciągu
    Returns: lista elementów ciągu Fibonacciego
    Throws: ValueError jeśli n <= 0
    """
    if n <= 0:
        raise ValueError("n musi być większe niż 0")
    wynik = [0, 1]
    if n == 1:
        return wynik[:1]
    a, b = 0, 1
    for _ in range(2, n):
        suma = a + b
        wynik.append(suma)
        a, b = b, suma
    return wynik[:n]


def fibonacci_rekurencja(n: int) -> list:
    """
    Generuje ciąg Fibonacciego metodą rekurencyjną z memoizacją.
    Parameters:
    n (int): liczba elementów ciągu
    Returns: lista elementów ciągu Fibonacciego
    Throws: ValueError jeśli n <= 0
    """
    if n <= 0:
        raise ValueError("n musi być większe niż 0")

    memo = {0: 0, 1: 1}

    def fib(k):
        if k not in memo:
            memo[k] = fib(k - 1) + fib(k - 2)
        return memo[k]

    return [fib(i) for i in range(n)]


def collatz(c0: int):
    """
    Generuje sekwencję Collatza od wartości początkowej c0.
    Parameters:
    c0 (int): wartość początkowa
    Returns: generator liczb w ciągu Collatza
    Throws: ValueError jeśli c0 <= 0
    """
    if c0 <= 0:
        raise ValueError("c0 musi być większe od 0")
    current = c0
    while current != 1:
        yield current
        if current % 2 == 0:
            current = current // 2
        else:
            current = 3 * current + 1
    yield 1


def komplement(dna: str) -> str:
    """
    Generuje nić komplementarną DNA.
    Parameters:
    dna (str): sekwencja DNA złożona z liter A, T, C, G
    Returns: nić komplementarna DNA
    Throws: ValueError jeśli sekwencja zawiera niedozwolone znaki
    """
    komplement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    if not all(ch in komplement for ch in dna):
        raise ValueError("Sekwencja DNA musi składać się z dozwolonych znaków -> ATCG")
    return ''.join(komplement[ch] for ch in dna)


def transkrybuj(dna: str) -> str:
    """
    Transkrybuje nić matrycową DNA do RNA.
    Parameters:
    dna (str): nić matrycowa DNA
    Returns: sekwencja RNA
    Throws: ValueError jeśli sekwencja zawiera niedozwolone znaki
    """
    trans = {'T': 'A', 'A': 'U', 'C': 'G', 'G': 'C'}
    if not all(ch in trans for ch in dna):
        raise ValueError("Sekwencja DNA musi składać się z dozwolonych znaków -> ATCG")
    return ''.join(trans[ch] for ch in dna)


if __name__ == "__main__":
    try:
        print("Pole trójkąta obliczone wzorem Herona:", heron(3.0, 4.0, 5.0))
        print("Część wspólna dwóch list:", wspolne([2, 2, 2, 2, 32, 4, 5, 6], [3, 4, 5, 6, 2, 2, 2, 7, 8]))
        print("Podzbiory zbioru {1, 2, 3, 5}:", podzbiory({1, 2, 3, 5}))
        print("Ciag Fibonacciego (iteracja):", fibonacci_iteracja(11))
        print("Ciag Fibonacciego (rekurencja):", fibonacci_rekurencja(11))

        c0 = 100
        kol = list(collatz(c0))
        print("Sekwencja Collatz:", ', '.join(str(x) for x in collatz(c0)))
        print("Maksymalna wartość:", max(kol))
        print("Długość ciągu:", len(kol))

        dna_kod = "ATGATCTCGTAA"
        dna_kod2 = "AGTGGATTCA"
        dna_matryca = komplement(dna_kod)
        dna_matryca2 = komplement(dna_kod2)
        dna_transkrybowane = transkrybuj(dna_matryca)
        dna_transkrybowane2 = transkrybuj(dna_matryca2)

        print("Nic kodująca DNA:", dna_kod)
        print("Nic matrycowa DNA:", dna_matryca)
        print("Nic transkrybowana RNA:", dna_transkrybowane)
        print("Druga próbka DNA:")
        print("Nic kodująca DNA:", dna_kod2)
        print("Nic matrycowa DNA:", dna_matryca2)
        print("Nic transkrybowana RNA:", dna_transkrybowane2)
    except ValueError as e:
        print("Błąd:", e)

