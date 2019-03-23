class ValidInput(object):

    def test_correctness_valueForSmallIndices(self):
        self.assertEqual(1, self.base_function(0))
        self.assertEqual(1, self.base_function(1))
        self.assertEqual(2, self.base_function(2))
        self.assertEqual(6, self.base_function(3))
        self.assertEqual(25852016738884976640000, self.base_function(23))

    def test_correctness_differentIntegerRepresentation_forInt18(self):
        self.assertEqual(6402373705728000, self.base_function(0x12))
        self.assertEqual(6402373705728000, self.base_function(0o22))
        self.assertEqual(6402373705728000, self.base_function(0b10010))

    def test_correctness_fakeTupleOfOne(self):
        # this is not a tuple, but int; tuple is defined by comma
        self.assertEqual(24, self.base_function((4)))


class ExceptionHandling(object):

    def test_wrongValue_negativeIntegers(self):
        with self.assertRaises(ValueError): self.base_function(-2)

    def test_wrongType_lookLikeInteger(self):
        with self.assertRaises(TypeError): self.base_function(3.0)
        with self.assertRaises(TypeError): self.base_function(0.0)
        with self.assertRaises(TypeError): self.base_function(-23.0)

    def test_wrongType_obviousFloat(self):
        with self.assertRaises(TypeError): self.base_function(3.5)
        with self.assertRaises(TypeError): self.base_function(-2.5)

    def test_wrongType_string(self):
        with self.assertRaises(TypeError): self.base_function("a")

    def test_wrongType_array(self):
        with self.assertRaises(TypeError): self.base_function([])
        with self.assertRaises(TypeError): self.base_function([4])
        with self.assertRaises(TypeError): self.base_function([4, 3])

    def test_wrongType_dictionary(self):
        with self.assertRaises(TypeError): self.base_function({})
        with self.assertRaises(TypeError): self.base_function({10: 40})

    def test_wrongType_tuple(self):
        with self.assertRaises(TypeError): self.base_function(())
        with self.assertRaises(TypeError): self.base_function((1,))
        with self.assertRaises(TypeError): self.base_function((2, 3))
