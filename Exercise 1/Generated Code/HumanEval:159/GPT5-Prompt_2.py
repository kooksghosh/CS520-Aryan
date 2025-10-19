def eat(number, need, remaining):
    """
    You're a hungry rabbit, and you already have eaten a certain number of carrots, but now you need to eat more carrots to complete the day's meals.
    You should return an array of [ total number of eaten carrots after your meals, the number of carrots left after your meals ].
    """
    if remaining >= need:
        number += need
        remaining -= need
    else:
        number += remaining
        remaining = 0
    return [number, remaining]


# --- Simple tests ---
if __name__ == "__main__":
    print(eat(5, 6, 10))   # [11, 4]
    print(eat(4, 8, 9))    # [12, 1]
    print(eat(1, 10, 10))  # [11, 0]
    print(eat(2, 11, 5))   # [7, 0]

    # Assertions (for automated check)
    assert eat(5, 6, 10) == [11, 4]
    assert eat(4, 8, 9) == [12, 1]
    assert eat(1, 10, 10) == [11, 0]
    assert eat(2, 11, 5) == [7, 0]
    print("All tests passed!")
