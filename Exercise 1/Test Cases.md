# Test Cases Used
---
## 1. HumanEval/155
```
print(even_odd_count(-12))    # (1, 1)
print(even_odd_count(123))    # (1, 2)
print(even_odd_count(0))      # (1, 0)
print(even_odd_count(2468))   # (4, 0)
print(even_odd_count(13579))  # (0, 5)
```

---

## 2. HumanEval/101
```
print(words_string('one,two,three'))              # ['one', 'two', 'three']
print(words_string('one two three'))              # ['one', 'two', 'three']
print(words_string('one, two,  three'))           # ['one', 'two', 'three']
print(words_string('  alpha,beta , gamma'))       # ['alpha', 'beta', 'gamma']
print(words_string('word'))                       # ['word']
```

---

## 3. HumanEval/132
```
print(is_nested('[]'))          # False — simple pair, not nested
print(is_nested('[[]]'))        # True — one bracket inside another
print(is_nested('[[[]]]'))      # True — deeper nesting
print(is_nested('[][[]]'))      # True — second pair is nested
print(is_nested(']]][[['))      # False — unbalanced
print(is_nested(''))            # False — empty string
```

---

## 4. HumanEval/136
```
assert largest_smallest_integers([-5, -1, 2, 3]) == (-1, 2)
assert largest_smallest_integers([1][2][3]) == (None, 1)
assert largest_smallest_integers([-10, -3, -4, 0]) == (-3, None)
assert largest_smallest_integers() == (None, None)
assert largest_smallest_integers([4]) == (None, 5)
assert largest_smallest_integers([-5]) == (-5, None)
assert largest_smallest_integers([-2, -2, 2, 2]) == (-2, 2)
```

---

## 5. HumanEval/156
```
assert int_to_mini_roman(19) == "xix"
assert int_to_mini_roman(152) == "clii"
assert int_to_mini_roman(426) == "cdxxvi"
assert int_to_mini_roman(4) == "iv"
assert int_to_mini_roman(944) == "cmxliv"
assert int_to_mini_roman(1000) == "m"
```

---

## 6. HumanEval/160
```
assert do_algebra(['+', '*', '-'], [2][3][5][4]) == 9            # 2 + 3*4 - 5
assert do_algebra(['**', '+'], [2][3][5]) == 12                  # 2**3 + 4
assert do_algebra(['//', '+', '*'], [6][3][2][4]) == 16         # 20//3 + 2*5
assert do_algebra(['-', '-', '-'], [7][2][3][5]) == 1           # 10 - 2 - 3 - 4
assert do_algebra(['*', '**'], [2][3][2]) == 18                  # 2*3**2
```

---

## 7. HumanEval/159
```
print(eat(5, 6, 10))   # [8][5]
print(eat(4, 8, 9))    # [9][1]
print(eat(1, 10, 10))  # [8]
print(eat(2, 11, 5))   # [10]
```

---

## 8. HumanEval/139
```
print(special_factorial(1))   # 1
print(special_factorial(2))   # 2
print(special_factorial(3))   # 12
print(special_factorial(4))   # 288
```

---

## 9. HumanEval/141
```
assert file_name_check("example.txt") == "Yes"
assert file_name_check("1example.dll") == "No"         # starts with digit
assert file_name_check("ex2a3m4ple.txt") == "Yes"      # exactly 3 digits
assert file_name_check("ex2a3m4p5le.txt") == "No"      # 4 digits
assert file_name_check("file.tar.gz") == "No"          # more than one dot
assert file_name_check(".txt") == "No"                 # empty before-dot
assert file_name_check("exa.mple.txt") == "No"         # extra dot before
assert file_name_check("example.pdf") == "No"          # invalid extension
```

---

## 10. HumanEval/151
```
assert double_the_difference([1][3][2]) == 10              # 1^2 + 3^2
assert double_the_difference([-1, -2, 0]) == 0
assert double_the_difference([9, -2]) == 81
assert double_the_difference() == 0
assert double_the_difference([]) == 0
assert double_the_difference([1.5, 3.0, 5]) == 25             # 3.0 ignored (not int), 5^2
assert double_the_difference([True, False, 7]) == 49          # bools ignored
```

