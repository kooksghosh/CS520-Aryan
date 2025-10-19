def is_nested(s: str) -> bool:
    """
    Return True iff there exists a valid nested bracket *subsequence*.
    Detect the minimal nested pattern "[[]]" as a subsequence (in order).
    """
    target = "[[]]"
    j = 0
    for ch in s:
        if j < len(target) and ch == target[j]:
            j += 1
            if j == len(target):
                return True
    return False


# --- Self-tests ---
if __name__ == "__main__":
    # should be True
    assert is_nested("[[]]")        is True
    assert is_nested("[][[]]")      is True
    assert is_nested("][][[]][")    is True
    assert is_nested("[[]][")       is True

    # should be False
    assert is_nested("[]")          is False
    assert is_nested("[][]")        is False
    assert is_nested("[[[]")        is False
    assert is_nested("]]][[[")      is False

    print("All tests passed!")
