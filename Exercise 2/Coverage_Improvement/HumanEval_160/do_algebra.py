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
    return eval(expr, {"__builtins__": None}, {})

