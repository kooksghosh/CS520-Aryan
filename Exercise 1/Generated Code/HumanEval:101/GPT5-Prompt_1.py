import re

def words_string(s):
    """
    Split a string by commas and/or whitespace and return a list of words.

    Examples:
      words_string("red, blue green")     -> ["red", "blue", "green"]
      words_string("  apple,, banana  ")  -> ["apple", "banana"]
      words_string("a,b,c")               -> ["a", "b", "c"]
    """
    # Replace any run of commas/whitespace with a single space, then split
    return [w for w in re.split(r"[,\s]+", s.strip()) if w]


if __name__ == "__main__":
    import sys
    s = sys.argv[1]  # pass the whole string as one argument (wrap in quotes)
    print(words_string(s))
