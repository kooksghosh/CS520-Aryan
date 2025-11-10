def even_odd_count(num):
    """
    Given an integer, return a tuple (even_count, odd_count) for its digits.
    Examples:
      even_odd_count(-12) -> (1, 1)
      even_odd_count(123) -> (1, 2)
    """
    s = str(abs(num))  # Ignore sign, convert to string
    even = 0
    odd = 0
    for ch in s:
        d = int(ch)
        if d % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)

