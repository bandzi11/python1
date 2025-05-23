import unittest
from lista import heron, wspolne, podzbiory, fibonacci_iteracja, fibonacci_rekurencja, collatz, komplement, transkrybuj


class TestFunkcje(unittest.TestCase):

    def test_heron(self):
        self.assertAlmostEqual(heron(3, 4, 5), 6.0)
        with self.assertRaises(ValueError):
            heron(1, 2, 3)  # nie tworzy trójkąta

    def test_wspolne(self):
        x = [1, 2, 2, 2, 2, 3, 4, 5, 6]
        y = [3, 4, 5, 6, 2, 2, 2, 7, 8, 9]
        result = wspolne(x, y)
        self.assertCountEqual(result, [2, 2, 2, 3, 4, 5, 6])
        with self.assertRaises(ValueError):
            wspolne([], [1, 2])
        with self.assertRaises(ValueError):
            wspolne([1, 2], [])

    def test_podzbiory(self):
        zbior = {1, 2}
        wynik = podzbiory(zbior)
        oczekiwane = [set(), {1}, {2}, {1, 2}]
        self.assertEqual(sorted(wynik, key=lambda s: (len(s), sorted(s))), sorted(oczekiwane, key=lambda s: (len(s), sorted(s))))

    def test_fibonacci_iteracja(self):
        self.assertEqual(fibonacci_iteracja(5), [0, 1, 1, 2, 3])
        with self.assertRaises(ValueError):
            fibonacci_iteracja(0)

    def test_fibonacci_rekurencja(self):
        self.assertEqual(fibonacci_rekurencja(5), [0, 1, 1, 2, 3])
        with self.assertRaises(ValueError):
            fibonacci_rekurencja(0)

    def test_collatz(self):
        wynik = list(collatz(6))
        self.assertEqual(wynik[-1], 1)
        with self.assertRaises(ValueError):
            list(collatz(0))

    def test_komplement(self):
        self.assertEqual(komplement("ATGC"), "TACG")
        with self.assertRaises(ValueError):
            komplement("AXYZ")

    def test_transkrybuj(self):
        self.assertEqual(transkrybuj("TACG"), "AUGC")
        with self.assertRaises(ValueError):
            transkrybuj("TXYZ")


if __name__ == '__main__':
    unittest.main()
