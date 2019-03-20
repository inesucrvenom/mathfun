"""Test for fibonacci functions
http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibtable.html
"""

import unittest
from src.fibonacci_recursive import fibonacci


class Test_Logic_FibonacciRecursive(unittest.TestCase):
    def test_low_index(self):
        """Test for lower indices."""
        self.assertEqual(0, fibonacci(0))
        self.assertEqual(1, fibonacci(1))
        self.assertEqual(1, fibonacci(2))
        self.assertEqual(2, fibonacci(3))
        self.assertEqual(3, fibonacci(4))
        self.assertEqual(5, fibonacci(5))
        self.assertEqual(8, fibonacci(6))
        self.assertEqual(55, fibonacci(10))
        self.assertEqual(28657, fibonacci(23))

    def test_different_representation(self):
        """Ints given in various forms."""
        self.assertEqual(2584, fibonacci(0x12))   # f(18)
        self.assertEqual(2584, fibonacci(0o22))   # f(18)
        self.assertEqual(2584, fibonacci(0b10010))   # f(18)

        # tuple of one int is int, whoa, that's new for me :-o
        self.assertEqual(3, fibonacci((4)))

    def test_wrong_value(self):
        """Check wrong inputs by value."""
        with self.assertRaises(ValueError): fibonacci(-2)
        with self.assertRaises(ValueError): fibonacci((-2))

    def test_wrong_type(self):
        """Check wrong inputs by type."""
        # those who looks like int
        with self.assertRaises(TypeError): fibonacci(3.0)
        with self.assertRaises(TypeError): fibonacci(0.0)
        with self.assertRaises(TypeError): fibonacci(-23.0)

        # obvious floats
        with self.assertRaises(TypeError): fibonacci(3.5)
        with self.assertRaises(TypeError): fibonacci(-2.5)

        # other objects
        with self.assertRaises(TypeError): fibonacci("a")

        with self.assertRaises(TypeError): fibonacci([])
        with self.assertRaises(TypeError): fibonacci([4])
        with self.assertRaises(TypeError): fibonacci([4, 3])

        with self.assertRaises(TypeError): fibonacci({})
        with self.assertRaises(TypeError): fibonacci({10: 40})

        with self.assertRaises(TypeError): fibonacci(())
        with self.assertRaises(TypeError): fibonacci((2, 3))


if __name__ == '__main__':
    unittest.main()
