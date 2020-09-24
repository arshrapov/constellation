import unittest
from constellation import *


class OperationsOnCordsClass(unittest.TestCase):

    def TestSumOfTwoCords(self):
        cords_1 = Cords(3,5,6)
        cords_2 = Cords(4,5,9)
        answer = Cords(7,10,15)

        self.assertEqual(cords_1 + cords_2, answer)


