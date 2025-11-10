import pytest
from int_to_mini_roman import int_to_mini_roman

def test_examples():
    assert int_to_mini_roman(19) == "xix"
    assert int_to_mini_roman(152) == "clii"
    assert int_to_mini_roman(426) == "cdxxvi"
    assert int_to_mini_roman(4) == "iv"
    assert int_to_mini_roman(944) == "cmxliv"
    assert int_to_mini_roman(1000) == "m"

