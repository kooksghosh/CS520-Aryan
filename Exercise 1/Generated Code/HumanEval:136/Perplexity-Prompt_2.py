def largest_smallest_integers(lst):
    """
    Returns a tuple (a, b), where 'a' is the largest negative integer,
    and 'b' is the smallest positive integer in the list.
    If there is no negative or positive integer, returns None for that value.
    """
    # Step 1: Check if the list is empty
    if not lst:
        return (None, None)

    # Step 2: Create separate lists for negative and positive integers
    negatives = [x for x in lst if x < 0]
    positives = [x for x in lst if x > 0]

    # Step 3: Find the maximum value among negatives or None
    largest_negative = max(negatives) if negatives else None

    # Step 4: Find the minimum value among positives or None
    smallest_positive = min(positives) if positives else None

    # Step 5: Return the tuple
    return (largest_negative, smallest_positive)

print(largest_smallest_integers([3, -1, -4, 2, 0, 7]))      # (-1, 2)
print(largest_smallest_integers([-10, -5, -2]))             # (-2, None)
print(largest_smallest_integers([5, 8, 12]))                # (None, 5)
print(largest_smallest_integers([0, 0, 0]))                 # (None, None)
print(largest_smallest_integers([]))                        # (None, None)

