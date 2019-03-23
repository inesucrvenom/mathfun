import unittest
from test.run_lambda import invoke_lambda
import test.fibonacci.basetests_fibonacci as BT


def call_function(val: int) -> int:
    return invoke_lambda('lambda_fibonacci_recursive', {'n': val})


class Test_ValidInput(unittest.TestCase, BT.ValidInput):
    def base_function(self, val):
        return call_function(val)


class Test_ExceptionHandling(unittest.TestCase, BT.ExceptionHandling):
    def base_function(self, val):
        return call_function(val)


class Test_RunningTime(unittest.TestCase):

    def test_time(self):
        self.assertNotIsInstance(call_function(30), Exception)

    def test_timeout(self):
        with self.assertRaises(Exception): call_function(31)


if __name__ == '__main__':
    unittest.main()
