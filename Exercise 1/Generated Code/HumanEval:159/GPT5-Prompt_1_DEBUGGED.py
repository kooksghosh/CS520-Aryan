def eat(number, need, remaining):
    """
    You're a hungry rabbit, and you already have eaten a certain number of carrots, but now you need to eat more carrots to complete the day's meals.
    You should return an array of [ total number of eaten carrots after your meals, the number of carrots left after your meals ]
    If there are not enough remaining carrots, you will eat all remaining carrots, but will still be hungry.

    Example:
    eat(5, 6, 10) -> [11, 4]
    eat(4, 8, 9) -> [12, 1]
    eat(1, 10, 10) -> [11, 0]
    eat(2, 11, 5) -> [7, 0]
    """
    if need <= remaining:
        # There are enough carrots.
        return [number + need, remaining - need]
    else:
        # Not enough carrots; eat all that remain.
        return [number + remaining, 0]

if __name__ == "__main__":
    # Expected outputs from the prompt examples
    assert eat(5, 6, 10) == [11, 4]
    assert eat(4, 8, 9)  == [12, 1]
    assert eat(1, 10, 10) == [11, 0]
    assert eat(2, 11, 5) == [7, 0]

    print("All tests passed!")
