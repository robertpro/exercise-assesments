from __future__ import print_function


class NumberToWord(object):
    def __init__(self):
        """Initialize required vars"""
        self.lower = {
            0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
            9: 'nine',
            10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
            17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

        self.ten = {
            10: 'ten', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
            90: 'ninety'}

    def _lower(self, number):
        """
        :param number: int
        :return: str
        :returns the number name
        """
        return self.lower[number]

    def _ten(self, number):
        """
        Check if the number is a ten, and returns its value from self.ten
        if number is not a ten, get ten number and unit then returns the name of the number in words
        :param number: int
        :return: str
        :returns the number name
        """
        if number % 10 == 0:
            return self.ten[number]
        else:
            ten, unit = divmod(number, 10)
            ten = ten * 10
            ten, unit = self.ten[ten], self.lower[unit]
            return "{ten}-{unit}".format(ten=ten, unit=unit)

    def _hundred(self, number):
        """
        Check if the number is a hundred, and returns its value from a combination of self.lower and self.ten
        if number is not a hundred, get hundred, ten and unit then returns the name of the number in words
        :param number: int
        :return: str
        :returns the number name
        """
        hundred, ten = divmod(number, 100)
        if number % 100 == 0:
            return "{hundred} hundred".format(hundred=self.lower[hundred])
        else:
            return "{hundred} hundred and {ten}".format(hundred=self.lower[hundred], ten=self.get_number_name(ten))

    def get_number_name(self, number):
        """
        Maps the number to its parser
        :param number: int
        :return: str
        :returns the number name
        """
        if number < 20:
            return self._lower(number)
        elif number < 100:
            return self._ten(number)
        elif number < 1000:
            return self._hundred(number)


def print_number_name():
    number = input("Write a number: ")
    number_to_word = NumberToWord()
    name = number_to_word.get_number_name(number)
    print(name)


def main():
    while True:
        try:
            print_number_name()
        except NameError:
            print("Write a valid number please!")
        except KeyboardInterrupt:
            print("Exiting!")
            exit(0)


if __name__ == '__main__':
    main()
