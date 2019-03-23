"""Test for iterative Fibonacci function on AWS Lambda.

Basically tests both correctness and basic integration.

Deploy lambda to AWS before running this.
"""

import unittest
from test.run_lambda import invoke_lambda


def call_lambda(val: int) -> int:
    """Convert local call into more abstract one from manual_run"""
    result = invoke_lambda('lambda_fibonacci_iterative', {'n': val})
    return result


class TestLambda_FibonacciIterative_ValidInput(unittest.TestCase):
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


class TestLambda_FibonacciIterative_InvalidInput(unittest.TestCase):
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


class TestLambda_FibonacciIterative_Time(unittest.TestCase):
    """Test correctness on valid input, or check time/timeout."""

    def test_time_30(self):
        self.assertEqual(832040, call_lambda(30))

    def test_time_31(self):
        self.assertEqual(1346269, call_lambda(31))

    def test_time_32(self):
        self.assertEqual(2178309, call_lambda(32))

    def test_time_33(self):
        self.assertEqual(3524578, call_lambda(33))

    def test_time_34(self):
        self.assertEqual(5702887, call_lambda(34))

    def test_time_35(self):
        self.assertEqual(9227465, call_lambda(35))

    def test_time_36(self):
        self.assertEqual(14930352, call_lambda(36))

    def test_time_50(self):
        self.assertEqual(12586269025, call_lambda(50))

    def test_time_100(self):
        self.assertEqual(354224848179261915075, call_lambda(100))

    def test_time_200(self):
        self.assertEqual(280571172992510140037611932413038677189525,
                         call_lambda(200))

    def test_time_300(self):
        self.assertEqual(222232244629420445529739893461909967206666939096499764990979600,
                         call_lambda(300))

    def test_time_500(self):
        self.assertEqual(139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125,
                         call_lambda(500))

    def test_time_1000(self):
        self.assertEqual(43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875,
                         call_lambda(1000))

if __name__ == '__main__':
    unittest.main()
