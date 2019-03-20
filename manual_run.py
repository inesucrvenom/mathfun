from test_lambda.invoke_lambda import format_result

def run_all():
    """Create own lambda invocations"""
#    print(format_result('lambda_simple_test', {'n': 33, 'm': 64, 'a': 14}))
    print(1)
    print(format_result('lambda_fibonacci_recursive', {'n': 2}))
    print(2)
    if format_result('lambda_fibonacci_recursive', {'n': "a"}) == TypeError:
        print(3)
    print(4)
    print(format_result('lambda_fibonacci_recursive', {'n': "a"}))

if __name__ == '__main__':
    run_all()
