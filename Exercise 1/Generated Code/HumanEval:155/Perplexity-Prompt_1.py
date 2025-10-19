def even_odd_count(num):
    num = abs(num)  # Ignore the sign of the number
    even_count = 0
    odd_count = 0

    for digit in str(num):
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return (even_count, odd_count)

print(even_odd_count(-12))   # (1, 1)
print(even_odd_count(123))   # (1, 2)
print(even_odd_count(0))     # (1, 0)
print(even_odd_count(2468))  # (4, 0)
print(even_odd_count(13579)) # (0, 5)
