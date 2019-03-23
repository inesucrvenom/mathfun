from test.run_lambda import show_result


def run_all():
    """Create own lambda invocations"""

    print(show_result('lambda_fibonacci_recursive', {'n': 20}))
    print(show_result('lambda_fibonacci_iterative', {'n': 20}))

    print(show_result('lambda_factorial_recursive', {'n': 20}))
    print(show_result('lambda_factorial_iterative', {'n': 20}))


if __name__ == '__main__':
    run_all()
