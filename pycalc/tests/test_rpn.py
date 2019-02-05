#! /usr/bin/python

import unittest
from rpn import RPN


class TestRPN(unittest.TestCase):
    """
    Unit tests of RPN class.
    """

    _infix = '(0-2*2+1)(2.3/3.4+4)3-4.1*2.2(7+4)/2.24log10(3)4.3+pi'
    _postfix = [0, 2, 2, '*', '-', 1, '+', 2.3, 3.4, '/', 4, '+', '*', 3, '*', 4.1, 2.2, '*', 7, 4, '+', '*', 2.24,
                '/', 3, 'log10', '*', 4.3, '*', '-', 3.141592653589793, '+']
    _result = -129.822479623173

    _rpn = RPN("")

    def test_convert(self):
        self.assertEqual(self._postfix, self._rpn.convert(self._infix))

    def test_calculate(self):
        self.assertEqual(self._result, self._rpn.calculate(self._postfix))

    def test_convert_brackets_exception(self):
        self.assertRaises(Exception, self._rpn.convert, '(' + self._infix)

    def test_convert_unknown_function_exception(self):
        self.assertRaises(Exception, self._rpn.convert, self._infix + '*wrong(1)')


if __name__ == "__main__":
    unittest.main()
