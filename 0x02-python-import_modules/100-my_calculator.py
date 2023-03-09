#!/usr/bin/python3
import sys
from calculator_1 import add, mul, sub, div
len1 = len(sys.argv)
if __name__ == "__main__":
    if len1 != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        for i in range(1, len1):
            a = int(sys.argv[1])
            op = sys.argv[2]
            b = int(sys.argv[3])
            if op != '+' and op != '-' and op != '/' and op != '*':
                print("Unknown operator. Available operators: +, -, * and /")
                sys.exit(1)
            elif op == '+':
                print("{} + {} = {}".format(a, b, add(a, b)))
                break
            elif op == '-':
                print("{} - {} = {}".format(a, b, sub(a, b)))
                break
            elif op == '/':
                print("{} / {} = {}".format(a, b, div(a, b)))
                break
            elif op == '*':
                print("{} * {} = {}".format(a, b, mul(a, b)))
                break
