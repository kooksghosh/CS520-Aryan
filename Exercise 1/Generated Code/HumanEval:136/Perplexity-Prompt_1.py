def largest_smallest_integers(lst):
    """
    Returns a tuple (a, b), where 'a' is the largest negative integer,
    and 'b' is the smallest positive integer in the list.
    If there is no negative or positive integer, returns None for that value.
    """
    # Step 1: Separate negative and positive integers
    negatives = [x for x in lst if x < 0]
    positives = [x for x in lst if x > 0]

    # Step 2: Find largest negative and smallest positive
    largest_negative = max(negatives) if negatives else None
    smallest_positive = min(positives) if positives else None

    # Step 3: Return the result as a tuple
    return (largest_negative, smallest_positive)


print(largest_smallest_integers([3, -1, -4, 2, 0, 7]))      # (-1, 2)
print(largest_smallest_integers([-10, -5, -2]))             # (-2, None)
print(largest_smallest_integers([5, 8, 12]))                # (None, 5)
print(largest_smallest_integers([0, 0, 0]))                 # (None, None)
print(largest_smallest_integers([]))                        # (None, None)
