def double_the_difference(lst):
    """
    Returns the sum of squares of odd, positive integers in the list.
    Ignores negative numbers, zero, and non-integers.
    Returns 0 for empty input.
    """
    # Step 1: Filter for positive odd integers only
    filtered = [x for x in lst if isinstance(x, int) and x > 0 and x % 2 == 1]
    
    # Step 2: Square each and sum
    result = sum(x ** 2 for x in filtered)
    
    # Step 3: Return the result
    return result

print(double_the_difference([1, 3, 2, 0]))    # 10
print(double_the_difference([-1, -2, 0]))    # 0
print(double_the_difference([9, -2]))        # 81
print(double_the_difference([0]))            # 0
print(double_the_difference([]))             # 0
