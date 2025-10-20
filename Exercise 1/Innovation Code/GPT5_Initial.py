def eat(number, need, remaining):
    """
    Return [total_eaten_after_meals, carrots_left].
    If remaining < need, eat all remaining and leave 0.
    """
    eaten_now = min(need, remaining)
    total = number + eaten_now
    left = remaining - eaten_now
    return [total, left]


# --- Simple tests ---
if __name__ == "__main__":
    assert eat(5, 6, 10) == [11, 4]
    assert eat(4, 8, 9)  == [12, 1]
    assert eat(1, 10, 10) == [11, 0]
    assert eat(2, 11, 5) == [7, 0]
    print("All tests passed!")
