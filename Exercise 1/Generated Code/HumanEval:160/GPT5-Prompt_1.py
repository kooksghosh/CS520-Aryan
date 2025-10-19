def do_algebra(operator, operand):
    """
    Build and evaluate an infix expression from operators and operands.
    Supports: +, -, *, //, **

    Example:
      operator = ['+', '*', '-']
      operand  = [2, 3, 4, 5]
      -> evaluates 2 + 3 * 4 - 5 == 9
    """
    if len(operator) != len(operand) - 1:
        raise ValueError("len(operator) must be len(operand) - 1")

    allowed = {"+", "-", "*", "//", "**"}
    for op in operator:
        if op not in allowed:
            raise ValueError(f"unsupported operator: {op!r}")

    # Build an expression string that respects normal precedence rules.
    parts = [str(int(operand[0]))]
    for op, val in zip(operator, operand[1:]):
        parts.append(op)
        parts.append(str(int(val)))
    expr = " ".join(parts)

    # Evaluate safely: no builtins/locals; only operators in the string are used.
    return eval(expr, {"__builtins__": None}, {})


# --- Quick self-tests ---
if __name__ == "__main__":
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9            # 2 + 3*4 - 5
    assert do_algebra(['**', '+'], [2, 3, 4]) == 12                  # 2**3 + 4
    assert do_algebra(['//', '+', '*'], [20, 3, 2, 5]) == 16         # 20//3 + 2*5
    assert do_algebra(['-', '-', '-'], [10, 2, 3, 4]) == 1           # 10 - 2 - 3 - 4
    assert do_algebra(['*', '**'], [2, 3, 2]) == 18                  # 2*3**2
    print("All tests passed!")
