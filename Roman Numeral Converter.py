#   Roman numerals are the symbols used in a system of numerical notation based on the ancient Roman system.
#   The symbols are I, V, X, L, C, D, and M, standing respectively for 1, 5, 10, 50, 100, 500, and 1,000.

#   https://www.calculatorsoup.com/calculators/conversions/roman-numeral-converter.php
#   https://www.mathsisfun.com/roman-numerals.html

escape_codes = {
    "default": '\033[0m',
    "red": '\033[31m',
    "green": '\033[32m',
    "blue": '\033[34m'
}

roman_dict = {
    1: "I",
    4: "IV",
    5: "V",
    9: "IX",
    10: "X",
    40: "XL",
    50: "L",
    90: "XC",
    100: "C",
    400: "CD",
    500: "D",
    900: "CM",
    1000: "M"
}


def convert(arabic):
    # take an integer and return a Roman numeral in string format

    if arabic > 3999:
        print("Can't convert numbers greater than 3999")
        return None
    if arabic < 1:
        print("Can't convert zero or negative numbers")
        return None

    roman = ""

    while arabic > 0:
        largest_key = 0
        # find the largest key
        for key in sorted(roman_dict.keys(), reverse=True):
            if key <= arabic:
                largest_key = key
                break

        arabic -= largest_key
        roman += roman_dict[largest_key]

    return roman


def run_tests():
    # iterate over a dictionary of correct values and check if our results are the same

    correct_pairs = {
        1: "I",
        3: "III",
        4: "IV",
        8: "VIII",
        9: "IX",
        39: "XXXIX",
        40: "XL",
        246: "CCXLVI",
        789: "DCCLXXXIX",
        2023: "MMXXIII",
        3999: "MMMCMXCIX"
    }

    for number, expected in correct_pairs.items():
        result = convert(number)
        if result == expected:
            print(escape_codes["green"], f"Test passed for {number}")
        else:
            print(escape_codes["red"], f"Test failed for {number}. Expected {expected} got {result}")


def run_main():
    # take an input from the user and print the Roman numeral
    while True:
        print(escape_codes['default'], end='')
        number = int(input("Enter a number: "))
        roman = convert(number)
        print(escape_codes["red"], f"{number}", escape_codes["blue"], f"= {roman}")


# run_tests()
run_main()
