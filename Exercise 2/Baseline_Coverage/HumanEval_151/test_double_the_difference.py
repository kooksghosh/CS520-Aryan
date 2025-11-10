import pytest
from double_the_difference import double_the_difference

def test_examples():
    assert double_the_difference([1, 3, 2, 0]) == 10
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([0]) == 0
    assert double_the_difference([]) == 0
    assert double_the_difference([1.5, 3.0, 5]) == 25
    assert double_the_difference([True, False, 7]) == 49

