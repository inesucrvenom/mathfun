"""Ackermann recursive implementation"""


def ackermann(m: int, n: int) -> int:
    """Implement Ackermann function recursively.

    Raise:
    - TypeError for given non integers
    - ValueError for given negative integers
    """
    if type(m) is not int or type(n) is not int:
        raise TypeError("m and/or n isn't integer")
    if m < 0 or n < 0:
        raise ValueError("m and/or n is negative")

    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ackermann(m-1, 1)
    else:
        return ackermann(m-1, ackermann(m, n-1))


def lambda_handler(event, context):
    """Lambda function for recursive Ackermann function."""
    return ackermann(event["m"], event["n"])
