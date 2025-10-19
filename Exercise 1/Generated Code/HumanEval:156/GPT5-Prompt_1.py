def int_to_mini_roman(number: int) -> str:
    """
    Convert 1..1000 to lowercase Roman numerals.
    Examples:
      19  -> 'xix'
      152 -> 'clii'
      426 -> 'cdxxvi'
    """
    # (value, symbol)
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
    res = []
    for val, sym in pairs:
        if n == 0:
            break
        count, n = divmod(n, val)
        if count:
            res.append(sym * count)
    return "".join(res).lower()


if __name__ == "__main__":
    assert int_to_mini_roman(19) == "xix"
    assert int_to_mini_roman(152) == "clii"
    assert int_to_mini_roman(426) == "cdxxvi"
    assert int_to_mini_roman(4) == "iv"
    assert int_to_mini_roman(944) == "cmxliv"
    assert int_to_mini_roman(1000) == "m"
    print("All tests passed!")
