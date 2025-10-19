import sys
def even_odd_count(num):
    """
    Given an integer, return a tuple (even_count, odd_count) for its digits.
    Examples:
      even_odd_count(-12) -> (1, 1)
      even_odd_count(123) -> (1, 2)
    """
    s = str(abs(num))  # 1) ignore sign, 2) convert to string
    even = 0
    odd = 0
    for ch in s:       # 3) check each digit, 4) count
        d = int(ch)
        if d % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)  # 5) return tuple

if __name__ == "__main__":
    import sys
    n = int(sys.argv[1])          # first argument
    print(even_odd_count(n))


