def words_string(s):
    """
    Split a string by commas and/or spaces and return the list of words.
    """
    if not s:                      # 1) handle empty input
        return []
    # 2) make separators uniform, 3) split on whitespace, 4) split() drops empties
    return s.replace(",", " ").split()

if __name__ == "__main__":
    import sys
    s = sys.argv[1]  # pass your input in quotes
    print(words_string(s))
