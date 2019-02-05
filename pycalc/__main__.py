#! /usr/bin/python

# Pure-python command-line calculator implemented based on Reverse Polish Notation (postfix notation).

import argparse
from rpn import RPN

parser = argparse.ArgumentParser(prog='pycalc', description='Pure-python command-line calculator.')
parser.add_argument('expr', help='expression string to evaluate', metavar='EXPRESSION')
parser.add_argument('-m', '--use-modules', help='additional modules to use', metavar='MODULE', nargs='+',
                    dest='modules')
parser.add_argument('-p', help='display postfix expression', default=False, action='store_const', const=True,
                    dest='show_postfix')


def main():
    args = parser.parse_args()
    try:
        converter = RPN(args.modules)
        postfix_expression = converter.convert(args.expr)

        if args.show_postfix:
            print(postfix_expression)

        print(converter.calculate(postfix_expression))
    except Exception as exception:
        if str(exception) == 'brackets are not balanced':
            print('ERROR: ' + str(exception))
            exit(1)
        elif str(exception).startswith('No module named'):
            print('ERROR: ' + str(exception))
            exit(2)
        else:
            print('ERROR: ' + str(exception))
            exit(3)


main()
