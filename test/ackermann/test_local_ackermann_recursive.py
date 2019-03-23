import unittest
from src.lambda_ackermann_recursive import ackermann
import test.ackermann.basetests_ackermann as BT


def call_function(a: int, b: int) -> int:
    return ackermann(a, b)


class Test_ValidInput(unittest.TestCase, BT.ValidInput):
    def base_function(self, a, b):
        return call_function(a, b)


class Test_ExceptionHandling(unittest.TestCase, BT.ExceptionHandling):
    def base_function(self, a, b):
        return call_function(a, b)


class Test_RunningTime(unittest.TestCase):

    def test_time(self):
        self.assertNotIsInstance(call_function(3, 4), Exception)


    def test_recursion_error(self):
        with self.assertRaises(Exception): call_function(4, 3)


if __name__ == "__main__":
    unittest.main()