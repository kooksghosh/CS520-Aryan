def do_algebra(operator, operand):
    """
    Given two lists operator and operand, build the algebraic expression and return its evaluation.
    """
    # Step 1: Start with the first operand as a string
    expr = str(operand[0])

    # Step 2: For each operator and next operand, append to the expression string
    for op, num in zip(operator, operand[1:]):
        expr += f' {op} {num}'

    # Step 3: Evaluate the expression and return the result
    return eval(expr)

operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
print(do_algebra(operator, operand))  # Output: 9
