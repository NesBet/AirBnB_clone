#!/usr/bin/python3
"""Multiplies 2 numbers."""


def multiply_numbers(a, b):
    """
    Multiply two numbers and return the result.

    :param a: The first number to be multiplied.
    :param b: The second number to be multiplied.
    :return: The product of a and b.
    """

    result = a * b
    return result


if __name__ == "__main__":
    num1 = 5
    num2 = 7
    product = multiply_numbers(num1, num2)
    print(f"Product of {num1} and {num2} is {product}")
