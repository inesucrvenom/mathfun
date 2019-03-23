"""Factorial recursive implementation"""


def factorial(n: int) -> int:
    """Implement factorials recursively

    Raise:
    - TypeError for given non integers
    - ValueError for given negative integers
    """
    if type(n) is not int:
        raise TypeError("n isn't integer")
    if n < 0:
        raise ValueError("n is negative")

    if n == 0:
        return 1
    return n * factorial(n-1)


def lambda_handler(event, context):
    """Lambda function for recursive factorials"""
    return factorial(event["n"])
