import re

def words_string(s):
    """
    Split a string by commas and/or whitespace and return a list of words.

    Examples:
      words_string("red, blue green")     -> ["red", "blue", "green"]
      words_string("  apple,, banana  ")  -> ["apple", "banana"]
      words_string("a,b,c")               -> ["a", "b", "c"]
    """
    return [w for w in re.split(r"[,\s]+", s.strip()) if w]

