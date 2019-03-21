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

    result = 1
    for i in range(2, n+1):
        result = result * i

    return result


def lambda_handler(event, context):
    """Lambda function for recursive factorials
    """

    return factorial(event['n'])
