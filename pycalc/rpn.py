#! /usr/bin/python

from operations import Operations
from stack import Stack
from tokenize import tokenize, NUMBER, OP, NAME, N_TOKENS, TokenError
from io import BytesIO


class RPN:
    """
    Implementation of Reverse Polish Notation.
    """

    def __init__(self, custom_modules):
        self._operations = Operations(custom_modules)
        self._stack = Stack()
        self._output = []

    def convert(self, infix_expression):
        """
        Converts the given infix expression to the postfix expression.
        Implicit multiplication is supported.
        """
        self._stack.clean()
        self._output = []
        multiplication_possible = False

        try:
            for code, value, _, _, _ in tokenize(BytesIO(infix_expression.encode('utf-8')).readline):
                if code == OP or code == NAME or code == N_TOKENS:
                    if value == ')':
                        self.__get_operators_from_stack()
                        multiplication_possible = True

                    elif value == '(':
                        if multiplication_possible:
                            self.__push_operator_on_stack('*')
                        self._stack.push(value)
                        multiplication_possible = False

                    elif self._operations.is_supported(value):
                        if self.__is_constant(value):
                            self.__send_number_to_output(self._operations.get(value))
                        else:
                            if multiplication_possible and self.__priority(value) < self.__priority('*'):
                                self.__push_operator_on_stack('*')
                            self.__push_operator_on_stack(value)
                        multiplication_possible = False

                    elif value == ',':  # to support 2-arguments methods like round(1.234, 2)
                        multiplication_possible = False

                    else:
                        raise Exception('unknown function \'%s\'' % value)
                elif code == NUMBER:
                    if multiplication_possible:
                        self.__push_operator_on_stack('*')
                    self.__send_number_to_output(value)
                    multiplication_possible = True

            self.__get_operators_from_stack()  # if it is not empty at the end of parsing the expression
            return self._output
        except TokenError:
            raise Exception('brackets are not balanced')

    def calculate(self, postfix_expression):
        """
        Calculates given postfix expression.
        """
        _stack = []
        for char in postfix_expression:
            if self._operations.is_supported(char):
                self.__calculate_expression_from_the_top_of_stack(char)
            else:
                self._stack.push(char)
        return self._stack.peek()

    def __is_last_operator_on_stack_priority_lower(self, char):
        """
        Returns True if the priority of the operator from the top of the stack is lower than priority of given operator.
        """
        return self.__priority(self._stack.peek()) <= self.__priority(char)

    def __push_operator_on_stack(self, char):
        """
        Puts given operator to the top of the stack. If given operator has higher priority then the operator
        from the top of the stack then item from the stack is moved to the output.
        """
        if self._stack.is_empty() or self._stack.peek() == '(':
            self._stack.push(char)
        else:
            while not self._stack.is_empty() and self._stack.peek() is not '(' \
              and self.__is_last_operator_on_stack_priority_lower(char):
                self._output.append(self._stack.pop())
            self._stack.push(char)

    def __send_number_to_output(self, number):
        """
        Sends given number to the output.
        """
        if float.is_integer(float(number)):
            self._output.append(int(number))
        else:
            self._output.append(float(number))

    def __get_operators_from_stack(self):
        """
        Moves operator(s) from the top ot the stack to the output.
        First occurrence of '(' or the bottom of the stack ends this action.
        """
        while not self._stack.is_empty():
            if self._stack.peek() != '(':
                self._output.append(self._stack.pop())
            else:
                self._stack.pop()
                break

    def __priority(self, operation):
        """
        Returns the priority of the given operation.
        """
        return self._operations.priority(operation)

    def __is_constant(self, function):
        """
        Returns True if given function returns a constant value (pi, etc...).
        """
        return self._operations.number_of_arguments(function) == 0

    def __calculate_expression_from_the_top_of_stack(self, operation):
        """
        Calculates value of given operation with arguments from the stack and sends the results to the stack.
        """
        if self._operations.number_of_arguments(operation) == 1:
            self._stack.push(self._operations.get(operation)(self._stack.pop()))
        else:
            a = self._stack.pop()
            b = self._stack.pop()
            self._stack.push(self._operations.get(operation)(b, a))
