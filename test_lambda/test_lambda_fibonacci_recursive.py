"""Test for fibonacci functions on AWS Lambda

Deploy lambda to AWS before running this.
http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibtable.html
"""

import unittest
from test_lambda.invoke_lambda import invoke_lambda, create_parameters


def call_lambda(val: int) -> int:
    """Convert local call into more abstract one from manual_run"""
    result, status = invoke_lambda('lambda_fibonacci_recursive',
                                   create_parameters({'n': val}))
    return result

class Test_Fibonacci_Recursive(unittest.TestCase):
    """Test recursive implementation of Fibonacci on AWS Lambda.

    Test user input and ability to catch some exceptions.

    Note:
        Something from boto3 throws warning in the console:
        ResourceWarning: unclosed <ssl.SSLSocket...
        see more: https://github.com/boto/boto3/issues/454
        still open issue
    """

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

    # todo: when in lambda, it fails differently
    def test_wrongValue_negativeIntegers(self):
        with self.assertRaises(ValueError): call_lambda(-2)
        with self.assertRaises(ValueError): call_lambda((-2))

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

    def test_correctness_fakeTupleOfOne(self):
        # this is not a tuple, but int; tuple is defined by comma
        self.assertEqual(3, call_lambda((4)))


if __name__ == '__main__':
    unittest.main()
