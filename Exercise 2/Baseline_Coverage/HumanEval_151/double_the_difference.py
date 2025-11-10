def double_the_difference(lst):
    """
    Return the sum of squares of numbers in lst that are:
      - integers (not bools),
      - positive,
      - odd.
    Ignore negatives, zero, non-integers, and booleans.
    """
    return sum(
        x * x
        for x in lst
        if isinstance(x, int) and not isinstance(x, bool) and x > 0 and x % 2 == 1
    )

