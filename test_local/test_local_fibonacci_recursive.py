"""Test for fibonacci functions
http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibtable.html
"""

import unittest
from src.lambda_fibonacci_recursive import fibonacci


class Test_Fibonacci_Recursive(unittest.TestCase):
    """Test recursive implementation of Fibonacci
    """
    def test_correctness_valueForSmallIndices(self):
        self.assertEqual(0, fibonacci(0))
        self.assertEqual(1, fibonacci(1))
        self.assertEqual(1, fibonacci(2))
        self.assertEqual(2, fibonacci(3))
        self.assertEqual(3, fibonacci(4))
        self.assertEqual(5, fibonacci(5))
        self.assertEqual(8, fibonacci(6))
        self.assertEqual(55, fibonacci(10))
        self.assertEqual(28657, fibonacci(23))

    def test_correctness_differentIntegerRepresentation_forInt18(self):
        self.assertEqual(2584, fibonacci(0x12))
        self.assertEqual(2584, fibonacci(0o22))
        self.assertEqual(2584, fibonacci(0b10010))

    def test_wrongValue_negativeIntegers(self):
        with self.assertRaises(ValueError): fibonacci(-2)
        with self.assertRaises(ValueError): fibonacci((-2))

    def test_wrongType_lookLikeInteger(self):
        with self.assertRaises(TypeError): fibonacci(3.0)
        with self.assertRaises(TypeError): fibonacci(0.0)
        with self.assertRaises(TypeError): fibonacci(-23.0)

    def test_wrongType_obviousFloat(self):
        with self.assertRaises(TypeError): fibonacci(3.5)
        with self.assertRaises(TypeError): fibonacci(-2.5)

    def test_wrongType_string(self):
        with self.assertRaises(TypeError): fibonacci("a")

    def test_wrongType_array(self):
        with self.assertRaises(TypeError): fibonacci([])
        with self.assertRaises(TypeError): fibonacci([4])
        with self.assertRaises(TypeError): fibonacci([4, 3])

    def test_wrongType_dictionary(self):
        with self.assertRaises(TypeError): fibonacci({})
        with self.assertRaises(TypeError): fibonacci({10: 40})

    def test_wrongType_tuple(self):
        with self.assertRaises(TypeError): fibonacci(())
        with self.assertRaises(TypeError): fibonacci((1,))
        with self.assertRaises(TypeError): fibonacci((2, 3))

    def test_correctness_fakeTupleOfOne(self):
        # this is not a tuple, but int; tuple is defined by comma
        self.assertEqual(3, fibonacci((4)))


if __name__ == '__main__':
    unittest.main()
