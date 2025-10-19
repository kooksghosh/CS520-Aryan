def eat(number, need, remaining):
    """
    You're a hungry rabbit, and you already have eaten a certain number of carrots, but now you need to eat more carrots to complete the day's meals.
    You should return an array of [ total number of eaten carrots after your meals, the number of carrots left after your meals ]
    If there are not enough remaining carrots, you will eat all remaining carrots, but will still be hungry.
    """
    total = number + need
    left = max(0, remaining - need)
    return [total, left]


# --- Simple tests (one-liners) ---
if __name__ == "__main__":
    # Expected outputs from the prompt examples
    assert eat(5, 6, 10) == [11, 4]
    assert eat(4, 8, 9)  == [12, 1]
    assert eat(1, 10, 10) == [11, 0]
    assert eat(2, 11, 5) == [7, 0] #Failed test

    print("All tests passed!")
