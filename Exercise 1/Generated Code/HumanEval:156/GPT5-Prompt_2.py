def int_to_mini_roman(number: int) -> str:
    """
    Convert an integer (1..1000) to a lowercase Roman numeral string.
    Examples:
      19  -> 'xix'
      152 -> 'clii'
      426 -> 'cdxxvi'
    """
    if not (1 <= number <= 1000):
        raise ValueError("number must be in 1..1000")

    pairs = [
        (1000, "M"),
        (900,  "CM"),
        (500,  "D"),
        (400,  "CD"),
        (100,  "C"),
        (90,   "XC"),
        (50,   "L"),
        (40,   "XL"),
        (10,   "X"),
        (9,    "IX"),
        (5,    "V"),
        (4,    "IV"),
        (1,    "I"),
    ]

    n = number
    parts = []
    for val, sym in pairs:
        if n == 0:
            break
        count, n = divmod(n, val)
        if count:
            parts.append(sym * count)

    return "".join(parts).lower()


# --- Quick self-tests ---
if __name__ == "__main__":
    assert int_to_mini_roman(19) == "xix"
    assert int_to_mini_roman(152) == "clii"
    assert int_to_mini_roman(426) == "cdxxvi"
    assert int_to_mini_roman(4) == "iv"
    assert int_to_mini_roman(944) == "cmxliv"
    assert int_to_mini_roman(1000) == "m"
    print("All tests passed!")
