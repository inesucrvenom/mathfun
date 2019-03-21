from test_lambda.run_lambda import show_result

def run_all():
    """Create own lambda invocations"""

    # print(show_result('lambda_simple_test', {'n': 33, 'm': 64, 'a': 14}))
    # print(show_result('lambda_fibonacci_recursive', {'n': 2}))
    # print(show_result('lambda_fibonacci_recursive', {'n': "a"}))
    # print(show_result('lambda_fibonacci_recursive', {'n': "a"}))

    # print(show_result('lambda_fibonacci_recursive', {'k': 2}))
    # print(show_result('lambda_fibonacci_recursive', {'n': 2}))
    # print(show_result('lambda_fibonacci_recursive', {'n': -2}))

    # print(show_result('lambda_fibonacci_recursive', {'n': 2}))
    # print(show_result('lambda_fibonacci_recursive', {'n': -2}))
    # print(show_result('lambda_fibonacci_recursive', {'n': {}}))
    # print(show_result('lambda_fibonacci_recursive', {'n': 37}))


    # print(show_result('lambda_fibonacci_recursive', {'n': 29}))
    print(show_result('lambda_fibonacci_recursive', {'n': 31}))
    # print(show_result('lambda_fibonacci_recursive', {'n': 33}))
    # print(show_result('lambda_fibonacci_recursive', {'n': 37}))



if __name__ == '__main__':
    run_all()
