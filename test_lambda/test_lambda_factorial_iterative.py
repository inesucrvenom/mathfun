"""Test for iterative factorial function on AWS Lambda.

Basically tests both correctness and basic integration.

Deploy lambda to AWS before running this.
"""

import unittest
from test_lambda.run_lambda import invoke_lambda


def call_lambda(val: int) -> int:
    """Convert local call into more abstract one from manual_run"""
    result = invoke_lambda('lambda_factorial_iterative', {'n': val})
    return result


class Test_FactorialIterative_ValidInput(unittest.TestCase):
    """Test correctness on valid input."""

    def test_correctness_valueForSmallIndices(self):
        self.assertEqual(1, call_lambda(0))
        self.assertEqual(1, call_lambda(1))
        self.assertEqual(2, call_lambda(2))
        self.assertEqual(6, call_lambda(3))
        self.assertEqual(24, call_lambda(4))
        self.assertEqual(120, call_lambda(5))
        self.assertEqual(720, call_lambda(6))
        self.assertEqual(3628800, call_lambda(10))
        self.assertEqual(25852016738884976640000, call_lambda(23))

    def test_correctness_differentIntegerRepresentation_forInt18(self):
        self.assertEqual(6402373705728000, call_lambda(0x12))
        self.assertEqual(6402373705728000, call_lambda(0o22))
        self.assertEqual(6402373705728000, call_lambda(0b10010))

    def test_correctness_fakeTupleOfOne(self):
        # this is not a tuple, but int; tuple is defined by comma
        self.assertEqual(24, call_lambda((4)))


class Test_FactorialIterative_InvalidInput(unittest.TestCase):
    """Test of handling exceptions sent through Fibonnaci."""

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


class Test_FactorialIterative_Time(unittest.TestCase):
    """Test correctness on valid input, or check time/timeout."""

    def test_time_30(self):
        self.assertEqual(265252859812191058636308480000000,
                         call_lambda(30))

    def test_time_100(self):
        self.assertEqual(93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000,
                         call_lambda(100))

    def test_time_500(self):
        self.assertEqual(1220136825991110068701238785423046926253574342803192842192413588385845373153881997605496447502203281863013616477148203584163378722078177200480785205159329285477907571939330603772960859086270429174547882424912726344305670173270769461062802310452644218878789465754777149863494367781037644274033827365397471386477878495438489595537537990423241061271326984327745715546309977202781014561081188373709531016356324432987029563896628911658974769572087926928871281780070265174507768410719624390394322536422605234945850129918571501248706961568141625359056693423813008856249246891564126775654481886506593847951775360894005745238940335798476363944905313062323749066445048824665075946735862074637925184200459369692981022263971952597190945217823331756934581508552332820762820023402626907898342451712006207714640979456116127629145951237229913340169552363850942885592018727433795173014586357570828355780158735432768888680120399882384702151467605445407663535984174430480128938313896881639487469658817504506926365338175055478128640000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,
                         call_lambda(500))

    # all good
    def test_time_x(self):
        self.assertNotIsInstance(call_lambda(40000), Exception)

    def test_timeout(self):
        self.assertRaises(Exception, call_lambda(45000))

if __name__ == '__main__':
    unittest.main()
