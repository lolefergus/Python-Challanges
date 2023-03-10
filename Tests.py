import unittest
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
        matrix = [[0,1,0,0],[1,0,1,1],[0,1,0,1],[0,1,1,0]]
        self.assertEqual(AdjMatrix.MatrixAdjacency.is_adjacent(matrix, 0, 2), False)
        self.assertEqual(AdjMatrix.MatrixAdjacency.is_adjacent(matrix, 0, 1), True)
        self.assertEqual(AdjMatrix.MatrixAdjacency.is_adjacent(matrix, 2, 1), True)

    def testidMatrix(self):
        self.assertEqual(IdMatrix.IdentityMatrix.id_mtrx(0),[])
        self.assertEqual(IdMatrix.IdentityMatrix.id_mtrx(2),[[1, 0], [0, 1]])
        self.assertEqual(IdMatrix.IdentityMatrix.id_mtrx(-4),[[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]])
        self.assertEqual(IdMatrix.IdentityMatrix.id_mtrx("Word"),"Error")

    def testOversCalc(self):
        self.assertEqual(Overs.OversCalculator.total_overs(256),42.4)
        self.assertEqual(Overs.OversCalculator.total_overs(3),0.3)
        self.assertEqual(Overs.OversCalculator.total_overs(24),4)

    def testDigitCounter(self):
        self.assertEqual(RecDigitCount.DigitCounter.digits_count(24560),5)
        self.assertEqual(RecDigitCount.DigitCounter.digits_count(134),3)
        self.assertEqual(RecDigitCount.DigitCounter.digits_count(0),1)
        self.assertEqual(RecDigitCount.DigitCounter.digits_count(1),1)






if __name__ == '__main__':
    unittest.main()
