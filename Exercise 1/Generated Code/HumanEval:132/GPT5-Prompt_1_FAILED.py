def is_nested(s: str) -> bool:
    """
    Return True iff there exists a nested bracket structure.
    """
    depth = 0
    max_depth = 0
    for ch in s:
        if ch == '[':
            depth += 1
            if depth > max_depth:
                max_depth = depth
        else:  # assumes only ']'
            depth -= 1
            if depth < 0:
                return False
    return depth == 0 and max_depth >= 2

'''Test Cases Failed:
python3 -c "from is_nested import is_nested; print(is_nested('][][[]]['))"
# Expected True (contains '[[]]' as a subsequence); prints False 

python3 -c "from is_nested import is_nested; print(is_nested('[[]]['))"
# Expected True; prints False'''
