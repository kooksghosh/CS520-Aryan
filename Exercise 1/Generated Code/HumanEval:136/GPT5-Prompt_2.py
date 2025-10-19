def largest_smallest_integers(lst):
    """
    Return (largest_negative, smallest_positive) from lst.
    Zero is neither negative nor positive. If a side doesn't exist, return None.
    """
    negatives = [x for x in lst if x < 0]
    positives = [x for x in lst if x > 0]

    largest_negative = max(negatives) if negatives else None
    smallest_positive = min(positives) if positives else None

    return (largest_negative, smallest_positive)


# --- Quick self-tests ---
if __name__ == "__main__":
    assert largest_smallest_integers([-5, -1, 2, 3]) == (-1, 2)
    assert largest_smallest_integers([0, 1, 2, 3]) == (None, 1)
    assert largest_smallest_integers([-10, -3, -4, 0]) == (-3, None)
    assert largest_smallest_integers([0, 0, 0]) == (None, None)
    assert largest_smallest_integers([5]) == (None, 5)
    assert largest_smallest_integers([-5]) == (-5, None)
    assert largest_smallest_integers([-2, -2, 2, 2]) == (-2, 2)
    print("All tests passed!")
