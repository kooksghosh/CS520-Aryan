def even_odd_count(num):
    """
    Given an integer, return a tuple that has the number of even and odd digits respectively.

    Example:
    even_odd_count(-12) ==> (1, 1)
    even_odd_count(123) ==> (1, 2)
    """
    # Step 1: Take the absolute value of the number
    num = abs(num)

    # Step 2: Convert the number to a string
    num_str = str(num)

    # Step 3: Initialize counters for even and odd digits
    even_count = 0
    odd_count = 0

    # Step 4: Check each digit
    for digit in num_str:
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    # Step 5: Return the result
    return (even_count, odd_count)

print(even_odd_count(-12))   # (1, 1)
print(even_odd_count(123))   # (1, 2)
print(even_odd_count(0))     # (1, 0)
print(even_odd_count(2468))  # (4, 0)
print(even_odd_count(13579)) # (0, 5)