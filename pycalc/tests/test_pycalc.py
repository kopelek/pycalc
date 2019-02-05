#! /usr/bin/python

import unittest
from rpn import RPN


class TestPyCalc(unittest.TestCase):
    """
    Unit tests of the whole program.
    """

    _rpn = RPN("")

    def test1(self):
        self.assertEqual(1.0, self._rpn.calculate(self._rpn.convert('sin(pi/2)')))

    def test2(self):
        self.assertEqual(14, self._rpn.calculate(self._rpn.convert('2(5+2)')))

    def test3(self):
        self.assertEqual(21, self._rpn.calculate(self._rpn.convert('(1 + 2)(3 + 4)')))

    def test4(self):
        self.assertEqual(5, self._rpn.calculate(self._rpn.convert('log10(10)5')))


if __name__ == "__main__":
    unittest.main()
