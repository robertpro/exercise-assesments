from __future__ import print_function


class NumberToWord(object):
    def __init__(self, number):
        self.number = number
        self.lower = {
            0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
            9: 'nine',
            10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
            17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

        self.ten = {
            10: 'ten', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
            90: 'ninety'}

    def _lower(self):
        return self.lower[self.number]

    def get_number_name(self):
        if self.number < 20:
            return self._lower()


def print_number_name():
    number = input("Write a number: ")
    number_to_word = NumberToWord(number)
    name = number_to_word.get_number_name()
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
