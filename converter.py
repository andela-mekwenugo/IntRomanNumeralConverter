import argparse

parser = argparse.ArgumentParser(
    description='Integer Conversion to Roman Numeral')


class IntergerToRomanNumeral(object):
    """Class to convert Interger To RomanNumeral."""

    def __init__(self, inp):
        """Initialize inp and type of inp."""
        self.inp = inp
        if not isinstance(inp, int):
            raise TypeError("Please enter an integer")

        # Numbers less than zero and greater than 3,999 are not represented.
        if not 0 < inp < 4000:
            raise ValueError("Integer input must be between 1 and 3999")

    def convert_int_to_numeral(self):
        """Convert an integer to a Roman numeral."""
        ints_constants = (
            1000, 900, 500, 400, 100, 90,
            50, 40, 10, 9, 5, 4, 1)
        nums = (
            'M', 'CM', 'D', 'CD', 'C', 'XC',
            'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
        result = []
        for i in range(len(ints_constants)):
            count = int(self.inp / ints_constants[i])
            result.append(nums[i] * count)
            self.inp -= ints_constants[i] * count
        return ''.join(result)


if __name__ == '__main__':
    parser.add_argument('input', type=int, help='Integer to be converted')
    args = parser.parse_args()
    my_class = IntergerToRomanNumeral(args.input)
    print(my_class.convert_int_to_numeral())
