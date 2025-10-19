def double_the_difference(lst):
    """
    Returns the sum of squares of odd, positive integers in the list.
    Ignores negative numbers, zero, and non-integers.
    Returns 0 for empty input.
    """
    # Step 1: Check if the input list is empty
    if not lst:
        return 0

    # Step 2: Filter for positive odd integers only
    filtered = [x for x in lst if isinstance(x, int) and x > 0 and x % 2 == 1]

    # Step 3: Square each element in the filtered list
    squared = [x ** 2 for x in filtered]

    # Step 4: Sum the squared values and return the result
    return sum(squared)

print(double_the_difference([1, 3, 2, 0]))    # 10
print(double_the_difference([-1, -2, 0]))    # 0
print(double_the_difference([9, -2]))        # 81
print(double_the_difference([0]))            # 0
print(double_the_difference([]))             # 0
