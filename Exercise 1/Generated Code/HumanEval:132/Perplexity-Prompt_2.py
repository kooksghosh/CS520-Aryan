def is_nested(string):
    """
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets where at least one bracket in the subsequence is nested.
    """
    # Step 1: Check if the string is empty
    if not string:
        return False

    # Step 2: Use a stack to track brackets and nesting depth
    depth = 0
    nested_found = False

    # Step 3: Scan the string
    for char in string:
        if char == '[':
            depth += 1
            # Step 4: If depth exceeds 1, nesting exists
            if depth > 1:
                nested_found = True
        elif char == ']':
            depth -= 1
            # If depth goes negative, brackets are not well-formed
            if depth < 0:
                return False

    # Step 5: Check for well-formedness and nesting
    return depth == 0 and nested_found

print(is_nested('[]'))        # False
print(is_nested('[[]]'))      # True
print(is_nested('[[[]]]'))    # True
print(is_nested('[][[]]'))    # True
print(is_nested(']]][[['))    # False
print(is_nested(''))          # False
