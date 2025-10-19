def eat(number, need, remaining):
    """
    Returns [total carrots eaten after meals, carrots left after meals].
    If not enough carrots remain, eat all remaining carrots.
    """
    # Step 1: Check if the need can be satisfied
    if need <= remaining:
        total_eaten = number + need
        carrots_left = remaining - need
    else:
        # Not enough carrots, eat all remaining
        total_eaten = number + remaining
        carrots_left = 0
    return [total_eaten, carrots_left]

print(eat(5, 6, 10))   # [11, 4]
print(eat(4, 8, 9))    # [12, 1]
print(eat(1, 10, 10))  # [11, 0]
print(eat(2, 11, 5))   # [7, 0]
