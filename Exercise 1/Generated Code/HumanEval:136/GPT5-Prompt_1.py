def largest_smallest_integers(lst):
    """
    Return (largest_negative, smallest_positive) from lst.
    If no negatives or no positives exist, return None for that side.
    Zero is treated as neither negative nor positive.
    """
    largest_negative = None
    smallest_positive = None

    for x in lst:
        if x < 0:
            if largest_negative is None or x > largest_negative:
                largest_negative = x
        elif x > 0:
            if smallest_positive is None or x < smallest_positive:
                smallest_positive = x

    return (largest_negative, smallest_positive)

if __name__ == "__main__":
    # basic cases
    assert largest_smallest_integers([-5, -1, 2, 3]) == (-1, 2)
    assert largest_smallest_integers([0, 1, 2, 3]) == (None, 1)
    assert largest_smallest_integers([-10, -3, -4, 0]) == (-3, None)
    assert largest_smallest_integers([0, 0, 0]) == (None, None)
    assert largest_smallest_integers([5]) == (None, 5)
    assert largest_smallest_integers([-5]) == (-5, None)
    assert largest_smallest_integers([-2, -2, 2, 2]) == (-2, 2)
    print("All tests passed!")
