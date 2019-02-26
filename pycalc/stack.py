#!/usr/bin/python3


class Stack(object):
    """
    Implementation of the stack structure.
    """

    def __init__(self):
        self._items = []

    def clean(self):
        """
        Removes all items.
        """
        self._items = []

    def push(self, item):
        """
        Adds given item at the top of the stack.
        """
        self._items.append(item)

    def pop(self):
        """
        Returns with removing from the stack the first item from the top of the stack.
        """
        return self._items.pop()

    def peek(self):
        """
        Returns the first item from the top of the stack.
        """
        return self._items[len(self._items) - 1]

    def is_empty(self):
        """
        Returns True if stack is empty, False otherwise.
        """
        return self._items == []
