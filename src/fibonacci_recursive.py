"""Fibonacci"""


def fibonacci(n: int) -> int:
    """Implement Fibonacci(n) recursively"""

    if type(n) is not int:
        raise TypeError("n isn't integer")
    if n < 0:
        raise ValueError("n is negative")

    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)


def my_handler(event, context):
    """Lambda function for recursive Fibonacci"""

