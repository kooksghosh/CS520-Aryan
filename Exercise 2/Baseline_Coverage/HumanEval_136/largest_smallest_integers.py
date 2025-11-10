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

