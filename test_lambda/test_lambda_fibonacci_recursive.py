"""Test for recursive Fibonacci function on AWS Lambda.

Basically tests both correctness and basic integration.

Deploy lambda to AWS before running this.

http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibtable.html
"""

import unittest
from test_lambda.run_lambda import invoke_lambda


def call_lambda(val: int) -> int:
    """Convert local call into more abstract one from manual_run"""
    result = invoke_lambda('lambda_fibonacci_recursive', {'n': val})
    return result


class TestLambda_FibonacciRecursive_validInput(unittest.TestCase):
    """Test correctness on valid input."""

    def test_correctness_valueForSmallIndices(self):
        self.assertEqual(0, call_lambda(0))
        self.assertEqual(1, call_lambda(1))
        self.assertEqual(1, call_lambda(2))
        self.assertEqual(2, call_lambda(3))
        self.assertEqual(3, call_lambda(4))
        self.assertEqual(5, call_lambda(5))
        self.assertEqual(8, call_lambda(6))
        self.assertEqual(55, call_lambda(10))
        self.assertEqual(28657, call_lambda(23))

    def test_correctness_differentIntegerRepresentation_forInt18(self):
        self.assertEqual(2584, call_lambda(0x12))
        self.assertEqual(2584, call_lambda(0o22))
        self.assertEqual(2584, call_lambda(0b10010))

    def test_correctness_fakeTupleOfOne(self):
        # this is not a tuple, but int; tuple is defined by comma
        self.assertEqual(3, call_lambda((4)))


class TestLambda_FibonacciRecursive_invalidInput(unittest.TestCase):
    """Test of handling exceptions sent through the lambda."""

    def test_wrongValue_negativeIntegers(self):
        with self.assertRaises(ValueError): call_lambda(-2)

    def test_wrongType_lookLikeInteger(self):
        with self.assertRaises(TypeError): call_lambda(3.0)
        with self.assertRaises(TypeError): call_lambda(0.0)
        with self.assertRaises(TypeError): call_lambda(-23.0)

    def test_wrongType_obviousFloat(self):
        with self.assertRaises(TypeError): call_lambda(3.5)
        with self.assertRaises(TypeError): call_lambda(-2.5)

    def test_wrongType_string(self):
        with self.assertRaises(TypeError): call_lambda("a")

    def test_wrongType_array(self):
        with self.assertRaises(TypeError): call_lambda([])
        with self.assertRaises(TypeError): call_lambda([4])
        with self.assertRaises(TypeError): call_lambda([4, 3])

    def test_wrongType_dictionary(self):
        with self.assertRaises(TypeError): call_lambda({})
        with self.assertRaises(TypeError): call_lambda({10: 40})

    def test_wrongType_tuple(self):
        with self.assertRaises(TypeError): call_lambda(())
        with self.assertRaises(TypeError): call_lambda((1,))
        with self.assertRaises(TypeError): call_lambda((2, 3))


class TestLambda_FibonacciRecursive_time(unittest.TestCase):
    """Test correctness on valid input, or check time/timeout."""

    def test_time_30(self):
        self.assertEqual(832040, call_lambda(30))   # 11s

    def test_timeout(self):
        with self.assertRaises(RuntimeError): call_lambda(31)   # 15s


if __name__ == '__main__':
    unittest.main()
