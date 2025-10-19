def special_factorial(n):
    """
    The Brazilian factorial is defined as:
    special_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    Example:
    >>> special_factorial(4)
    288
    """
    if n <= 0:
        raise ValueError("n must be greater than 0")

    total = 1
    running_fact = 1

    for i in range(1, n + 1):
        running_fact *= i
        total *= running_fact

    return total


# --- Simple tests ---
if __name__ == "__main__":
    print(special_factorial(1))  # 1
    print(special_factorial(2))  # 2
    print(special_factorial(3))  # 12
    print(special_factorial(4))  # 288

    # Assertions
    assert special_factorial(1) == 1
    assert special_factorial(2) == 2
    assert special_factorial(3) == 12
    assert special_factorial(4) == 288
    print("All tests passed!")
