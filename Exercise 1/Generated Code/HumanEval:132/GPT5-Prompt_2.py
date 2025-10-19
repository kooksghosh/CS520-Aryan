def is_nested(s: str) -> bool:
    """
    Return True iff there exists a valid nested bracket subsequence.
    We only need to detect the minimal nested pattern "[[]]" as a subsequence
    (characters in order, not necessarily adjacent).
    """
    target = "[[]]"
    j = 0
    for ch in s:
        if ch == target[j]:
            j += 1
            if j == len(target):
                return True
    return False


def _self_tests():
    # True cases (contain a nested subsequence)
    assert is_nested("[[]]") is True
    assert is_nested("[][[]]") is True
    assert is_nested("][][[]][") is True          # unbalanced overall, subsequence exists
    assert is_nested("[[[[]]]]") is True
    assert is_nested("[][[[]]][]") is True
    assert is_nested("[]][[][[]][][") is True

    # False cases (no nested subsequence)
    assert is_nested("") is False
    assert is_nested("[]") is False
    assert is_nested("[][]") is False
    assert is_nested("]]]") is False
    assert is_nested("[[[]") is False             # no final closing ']'
    assert is_nested("][[][") is False            # order prevents completing "[[]]"

    print("All tests passed!")


if __name__ == "__main__":
    _self_tests()
