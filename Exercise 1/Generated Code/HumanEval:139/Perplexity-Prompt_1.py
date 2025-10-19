import math

def special_factorial(n):
    """
    Returns the Brazilian factorial: n! * (n-1)! * ... * 1!
    """
    result = 1
    for i in range(1, n + 1):
        result *= math.factorial(i)
    return result

print(special_factorial(4))  # 288
