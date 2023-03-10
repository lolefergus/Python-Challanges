import unittest

import DictBuilder
import LineLn
from FizzBuzz import FizzBuzz
import AdjMatrix
import IdMatrix
import Overs
import RecDigitCount


class ChallengeTests(unittest.TestCase):

    def testFizz(self):
        self.assertEqual(FizzBuzz.fizz_buzz(0), "FizzBuzz")
        self.assertEqual(FizzBuzz.fizz_buzz(3), "Fizz")
        self.assertEqual(FizzBuzz.fizz_buzz(5), "Buzz")
        self.assertEqual(FizzBuzz.fizz_buzz(15), "FizzBuzz")
        self.assertEqual(FizzBuzz.fizz_buzz(11), "11")

    def testAdjacency(self):
        matrix = [[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]]
        self.assertEqual(AdjMatrix.MatrixAdjacency.is_adjacent(matrix, 0, 2), False)
        self.assertEqual(AdjMatrix.MatrixAdjacency.is_adjacent(matrix, 0, 1), True)
        self.assertEqual(AdjMatrix.MatrixAdjacency.is_adjacent(matrix, 2, 1), True)

    def testidMatrix(self):
        self.assertEqual(IdMatrix.IdentityMatrix.id_mtrx(0), [])
        self.assertEqual(IdMatrix.IdentityMatrix.id_mtrx(2), [[1, 0], [0, 1]])
        self.assertEqual(IdMatrix.IdentityMatrix.id_mtrx(-4), [[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]])
        self.assertEqual(IdMatrix.IdentityMatrix.id_mtrx("Word"), "Error")

    def testOversCalc(self):
        self.assertEqual(Overs.OversCalculator.total_overs(256), 42.4)
        self.assertEqual(Overs.OversCalculator.total_overs(3), 0.3)
        self.assertEqual(Overs.OversCalculator.total_overs(24), 4)

    def testDigitCounter(self):
        self.assertEqual(RecDigitCount.DigitCounter.digits_count(24560), 5)
        self.assertEqual(RecDigitCount.DigitCounter.digits_count(134), 3)
        self.assertEqual(RecDigitCount.DigitCounter.digits_count(0), 1)
        self.assertEqual(RecDigitCount.DigitCounter.digits_count(1), 1)

    def testLineLen(self):
        self.assertEqual(LineLn.line_length([0, 0], [10, 15]), 18.03)
        self.assertEqual(LineLn.line_length([0, 0], [-2, 15]), 15.13)
        self.assertEqual(LineLn.line_length([0, 0], [0, 0]), 0)
        self.assertEqual(LineLn.line_length([150, 34], [12, 11]), 139.90)

    def testDictBuilder(self):
        self.assertEqual(DictBuilder.top_note({"name": "John", "notes": [3, 5, 4]}), {"name": "John", "top_note": 5})
        self.assertEqual(DictBuilder.top_note({"name": "Max", "notes": [1, 4, 6]}), {"name": "Max", "top_note": 6})
        self.assertEqual(DictBuilder.top_note({"name": "Zygmund", "notes": [1, 2, 3]}), {"name": "Zygmund", "top_note": 3})


if __name__ == '__main__':
    unittest.main()
