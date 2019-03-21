"""Fibonacci recursive implementation"""


def fibonacci(n: int) -> int:
    """Implement Fibonacci recursively

    Raise:
    - TypeError for given non integers
    - ValueError for given negative integers
    """

    if type(n) is not int:
        raise TypeError("n isn't integer")
    if n < 0:
        raise ValueError("n is negative")

    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)


def lambda_handler(event, context):
    """Lambda function for recursive Fibonacci
    """

    return fibonacci(event['n'])
