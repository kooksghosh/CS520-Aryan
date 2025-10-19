def is_nested(string):
    """
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets where at least one bracket in the subsequence is nested.
    """
    # Step 1: Initialize tracking variables
    count = 0          # tracks current bracket depth
    nested_found = False  # flags when a nested structure appears

    # Step 2: Traverse through each character in the string
    for char in string:
        if char == '[':
            count += 1
            # If count > 1, nesting exists
            if count > 1:
                nested_found = True
        elif char == ']':
            count -= 1
            # Step 3: If count ever goes negative, brackets are unbalanced
            if count < 0:
                return False

    # Step 4: After traversal, check that brackets are balanced and nesting occurred
    return count == 0 and nested_found

print(is_nested('[]'))        # False — simple pair, not nested
print(is_nested('[[]]'))      # True — one bracket inside another
print(is_nested('[[[]]]'))    # True — deeper nesting
print(is_nested('[][[]]'))    # True — second pair is nested
print(is_nested(']]][[['))    # False — unbalanced
print(is_nested(''))          # False — empty string
