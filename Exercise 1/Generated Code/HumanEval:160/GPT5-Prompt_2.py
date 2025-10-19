def do_algebra(operator, operand):
    """
    Build and evaluate an infix expression from operators and operands.
    Supports: +, -, *, //, **
    """
    if len(operator) != len(operand) - 1:
        raise ValueError("len(operator) must be len(operand) - 1")

    # Construct the expression step by step
    expression = str(operand[0])
    for op, val in zip(operator, operand[1:]):
        expression += f" {op} {val}"

    # Safely evaluate the expression
    return eval(expression, {"__builtins__": None}, {})


# --- Self-tests ---
if __name__ == "__main__":
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9       # 2 + 3*4 - 5
    assert do_algebra(['**', '+'], [2, 3, 4]) == 12             # 2**3 + 4
    assert do_algebra(['//', '+', '*'], [20, 3, 2, 5]) == 16    # 20//3 + 2*5
    assert do_algebra(['-', '-', '-'], [10, 2, 3, 4]) == 1      # 10 - 2 - 3 - 4
    assert do_algebra(['*', '**'], [2, 3, 2]) == 18             # 2*3**2
    print("All tests passed!")
