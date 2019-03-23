import unittest
from src.lambda_fibonacci_iterative import fibonacci
import test.fibonacci.basetests_fibonacci as BT


def call_function(val: int) -> int:
    return fibonacci(val)


class Test_ValidInput(unittest.TestCase, BT.ValidInput):
    def base_function(self, val):
        return call_function(val)


class Test_ExceptionHandling(unittest.TestCase, BT.ExceptionHandling):
    def base_function(self, val):
        return call_function(val)


class Test_RunningTime(unittest.TestCase):

    def test_time(self):
        self.assertNotIsInstance(call_function(36), Exception)


if __name__ == "__main__":
    unittest.main()
