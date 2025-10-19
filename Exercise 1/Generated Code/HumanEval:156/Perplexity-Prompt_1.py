def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string, and return it in lowercase.
    Restrictions: 1 <= num <= 1000
    """
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    result = ''
    for value, symbol in zip(values, symbols):
        while number >= value:
            result += symbol
            number -= value
    return result.lower()

print(int_to_mini_roman(19))   # 'xix'
print(int_to_mini_roman(152))  # 'clii'
print(int_to_mini_roman(426))  # 'cdxxvi'
