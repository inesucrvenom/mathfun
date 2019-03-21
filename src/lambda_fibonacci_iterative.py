"""Fibonacci iterative implementation

https://stackoverflow.com/questions/14661633/finding-out-nth-fibonacci-number-for-very-large-n/
"""


def fibonacci(n: int) -> int:
    """Implement Fibonacci iteratively

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

    a = 0
    b = 1
    for i in range(2, n+1):
        a, b = b, a+b
    return b


def lambda_handler(event, context):
    """Lambda function for iterative Fibonacci"""

    return fibonacci(event['n'])
