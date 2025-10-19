def double_the_difference(lst):
    """
    Return the sum of squares of values in lst that are:
      - integers (not bools),
      - positive,
      - odd.
    Ignore negatives, zero, non-integers, and booleans.
    """
    if not lst:
        return 0
    return sum(
        x * x
        for x in lst
        if isinstance(x, int) and not isinstance(x, bool) and x > 0 and x % 2 == 1
    )


# --- Simple tests ---
if __name__ == "__main__":
    assert double_the_difference([1, 3, 2, 0]) == 10          # 1^2 + 3^2
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([0]) == 0
    assert double_the_difference([]) == 0
    assert double_the_difference([1.5, 3.0, 5]) == 25         # 3.0 ignored (not int), 5^2
    assert double_the_difference([True, False, 7]) == 49      # bools ignored
    print("All tests passed!")
