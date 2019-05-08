import unittest
from converter import IntergerToRomanNumeral


class TestIntConverter(unittest.TestCase):

    def _get_convertion_function(self, int):
        converter_class = IntergerToRomanNumeral(int)
        return converter_class.convert_int_to_numeral()

    def test_convert_string_to_numeral(self):
        result = self._get_convertion_function(22)
        self.assertEqual(result, 'XXII')

    def test_does_not_convert_non_string_to_numeral(self):
        with self.assertRaises(TypeError):
            self._get_convertion_function("Some_string")

    def test_does_not_convert_number_greater_than_3999(self):
        with self.assertRaises(ValueError):
            self._get_convertion_function(4000)


if __name__ == '__main__':
    unittest.main()
