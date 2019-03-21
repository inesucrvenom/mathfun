"""Test for iterative Fibonacci function"""

import unittest
from src.lambda_fibonacci_iterative import fibonacci


class Test_FibonacciIterative_ValidInput(unittest.TestCase):
    """Test correctness on valid input."""

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

    def test_correctness_fakeTupleOfOne(self):
        # this is not a tuple, but int; tuple is defined by comma
        self.assertEqual(3, fibonacci((4)))


class Test_FibonacciIterative_InvalidInput(unittest.TestCase):
    """Test of handling exceptions sent through Fibonnaci."""

    def test_wrongValue_negativeIntegers(self):
        with self.assertRaises(ValueError): fibonacci(-2)

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


class Test_FibonacciIterative_Time(unittest.TestCase):
    """Test correctness on valid input, or check time/timeout."""

    def test_time_30(self):
        self.assertEqual(832040, fibonacci(30))

    def test_time_31(self):
        self.assertEqual(1346269, fibonacci(31))

    def test_time_32(self):
        self.assertEqual(2178309, fibonacci(32))

    def test_time_33(self):
        self.assertEqual(3524578, fibonacci(33))

    def test_time_34(self):
        self.assertEqual(5702887, fibonacci(34))

    def test_time_35(self):
        self.assertEqual(9227465, fibonacci(35))

    def test_time_36(self):
        self.assertEqual(14930352, fibonacci(36))

    def test_time_50(self):
        self.assertEqual(12586269025, fibonacci(50))

    def test_time_100(self):
        self.assertEqual(354224848179261915075, fibonacci(100))

    def test_time_200(self):
        self.assertEqual(280571172992510140037611932413038677189525,
                         fibonacci(200))

    def test_time_300(self):
        self.assertEqual(222232244629420445529739893461909967206666939096499764990979600,
                         fibonacci(300))

    def test_time_500(self):
        self.assertEqual(139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125,
                         fibonacci(500))

    def test_time_1000(self):
        self.assertEqual(43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875,
                         fibonacci(1000))


if __name__ == '__main__':
    unittest.main()
