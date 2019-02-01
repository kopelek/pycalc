#! /usr/bin/python

import imp
import operator
import math


class Operations:
    """
    Operations with priorities and number of arguments to calculate.
    Supports operations from custom modules which name is provided in constructor.
    """

    def __init__(self, custom_modules):
        self.__get_operations_from_module(math)
        if custom_modules:
            for module_name in custom_modules:
                module = imp.load_module(module_name, *imp.find_module(module_name))
                self.__get_operations_from_module(module)

    _OPERATORS = {'+': [operator.add, 2, 2],
                  '-': [operator.sub, 2, 2],
                  '*': [operator.mul, 1, 2],
                  '/': [operator.truediv, 1, 2],
                  '//': [operator.floordiv, 1, 2],
                  '%': [operator.mod, 1, 2],
                  '<': [operator.lt, 3, 2],
                  '<=': [operator.le, 3, 2],
                  '==': [operator.eq, 3, 2],
                  '!=': [operator.ne, 3, 2],
                  '>=': [operator.ge, 3, 2],
                  '>': [operator.gt, 3, 2],
                  'abs': [operator.abs, 1, 1],
                  'round': [round.__call__, 1, 2]}

    def priority(self, operation):
        """
        Returns priority of given operation.
        """
        return self._OPERATORS[operation][1]

    def number_of_arguments(self, operation):
        """
        Returns number of arguments for given operation.
        """
        return self._OPERATORS[operation][2]

    def get(self, operation):
        """
        Returns callable function of given operation.
        """
        return self._OPERATORS[operation][0]

    def is_supported(self, operation):
        """
        Returns True if given operation is supported, False otherwise.
        """
        return operation in self._OPERATORS.keys()

    def __get_operations_from_module(self, module):
        """
        Adds all functions from given module to the list of supported operations.
        """
        for function_name in dir(module):
            if not function_name.startswith('__'):
                callable_function = getattr(module, function_name)
                arguments_count = self.__get_arguments_count(callable_function)
                self._OPERATORS.update({function_name: [callable_function, 0, arguments_count]})

    def __get_arguments_count(self, callable_function):
        """
        Returns the number of arguments of given callable_function base on __doc___.
        """
        if type(callable_function) is float:
            return 0
        else:
            function_doc_first_line = callable_function.__doc__.splitlines()[0]
            return function_doc_first_line.split(',').__len__()
