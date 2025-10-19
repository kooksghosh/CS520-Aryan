def int_to_mini_roman(number):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    result = ''
    for value, symbol in zip(values, symbols):
        count = number // value
        result += symbol * count
        number -= value * count
    return result.lower()

print(int_to_mini_roman(19))   # 'xix'
print(int_to_mini_roman(152))  # 'clii'
print(int_to_mini_roman(426))  # 'cdxxvi'

