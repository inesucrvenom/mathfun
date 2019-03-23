class ValidInput(object):

    def test_correctness_valueForSmallIndices(self):
        self.assertEqual(1, self.base_function(0, 0))
        self.assertEqual(2, self.base_function(0, 1))
        self.assertEqual(2, self.base_function(1, 0))
        self.assertEqual(3, self.base_function(1, 1))
        self.assertEqual(7, self.base_function(2, 2))
        self.assertEqual(61, self.base_function(3, 3))

class ExceptionHandling(object):

    def test_wrongValue_negativeIntegers(self):
        with self.assertRaises(ValueError): self.base_function(-2, -5)
        with self.assertRaises(ValueError): self.base_function(-2, 4)
        with self.assertRaises(ValueError): self.base_function(6, -5)

        with self.assertRaises(ValueError): self.base_function(0, -5)
        with self.assertRaises(ValueError): self.base_function(-7, 0)

    def test_wrongType_lookLikeInteger(self):
        with self.assertRaises(TypeError): self.base_function(3.0, 1)
        with self.assertRaises(TypeError): self.base_function(0.0, 0.0)
        with self.assertRaises(TypeError): self.base_function(-23.0, 5)

    def test_wrongType_obviousFloat(self):
        with self.assertRaises(TypeError): self.base_function(3.5, 2.7)
        with self.assertRaises(TypeError): self.base_function(-2.5, 5.3)

    def test_wrongType_string(self):
        with self.assertRaises(TypeError): self.base_function("a", "b")

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
