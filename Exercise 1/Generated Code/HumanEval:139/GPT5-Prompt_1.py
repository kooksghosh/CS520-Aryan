def special_factorial(n: int) -> int:
    """
    Brazilian factorial:
      special_factorial(n) = 1! * 2! * ... * n!
    Requires n >= 1.
    """
    if n < 1:
        raise ValueError("n must be >= 1")

    running_fact = 1   # holds k!
    result = 1         # product of 1! * 2! * ... * k!
    for k in range(1, n + 1):
        running_fact *= k     # k! = (k-1)! * k
        result *= running_fact
    return result


# --- Quick self-tests ---
if __name__ == "__main__":
    assert special_factorial(1) == 1                 # 1!
    assert special_factorial(2) == 2                 # 1!*2! = 2
    assert special_factorial(3) == 12                # 1!*2!*3! = 12
    assert special_factorial(4) == 288               # example
    assert special_factorial(5) == 34560
    print("All tests passed!")
