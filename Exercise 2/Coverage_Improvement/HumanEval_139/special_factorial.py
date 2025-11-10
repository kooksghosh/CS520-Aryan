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

