import unittest

from main import NumberToWord


class NumberToWordTestCase(unittest.TestCase):
    def __init__(self, methodName='test_number_to_word'):
        super(NumberToWordTestCase, self).__init__(methodName)
        self.number_to_word = NumberToWord()

    def _test(self, to_test, should_be_list):
        for i in range(len(to_test)):
            res = self.number_to_word.get_number_name(to_test[i])
            should_be = should_be_list[i]
            self.assertEqual(res, should_be)

    def test_unit(self):
        to_test = [4, 6, 9, 1]
        should_be_list = ['four', 'six', 'nine', 'one']
        self._test(to_test, should_be_list)

    def test_ten(self):
        to_test = [45, 63, 19, 91, 33, 65]
        should_be_list = ['forty-five', 'sixty-three', 'nineteen', 'ninety-one', 'thirty-three', 'sixty-five']
        self._test(to_test, should_be_list)

    def test_hundred(self):
        to_test = [435, 163, 219, 591, 833, 700]
        should_be_list = ['four hundred and thirty-five', 'one hundred and sixty-three', 'two hundred and nineteen',
                          'five hundred and ninety-one', 'eight hundred and thirty-three', 'seven hundred']
        self._test(to_test, should_be_list)

    def test_thousand(self):
        to_test = [1000, 4950, 2445, 6675, 5876, 9873, 9999, 99999, 999999]
        should_be_list = [
            'one thousand',
            'four thousand, nine hundred and fifty',
            'two thousand, four hundred and forty-five',
            'six thousand, six hundred and seventy-five',
            'five thousand, eight hundred and seventy-six',
            'nine thousand, eight hundred and seventy-three',
            'nine thousand, nine hundred and ninety-nine',
            'ninety-nine thousand, nine hundred and ninety-nine',
            'nine hundred and ninety-nine thousand, nine hundred and ninety-nine'
        ]
        self._test(to_test, should_be_list)


if __name__ == '__main__':
    unittest.main()
