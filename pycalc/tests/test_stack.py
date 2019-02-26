#!/usr/bin/python3

import unittest
from stack import Stack


class TestStack(unittest.TestCase):
    """
    Unit tests of Stack class.
    """

    _stack = Stack()

    def test_stack(self):
        self.assertEqual(True, self._stack.is_empty())
        self._stack.push(1)
        self._stack.push('a')
        self.assertEqual('a', self._stack.peek())
        self.assertEqual('a', self._stack.pop())
        self.assertEqual(1, self._stack.peek())
        self.assertEqual(False, self._stack.is_empty())
        self._stack.clean()
        self.assertEqual(True, self._stack.is_empty())


if __name__ == "__main__":
    unittest.main()
