import pytest
from largest_smallest_integers import largest_smallest_integers

def test_examples():
    assert largest_smallest_integers([-5, -1, 2, 3]) == (-1, 2)
    assert largest_smallest_integers([0, 1, 2, 3]) == (None, 1)
    assert largest_smallest_integers([-10, -3, -4, 0]) == (-3, None)
    assert largest_smallest_integers([0, 0, 0]) == (None, None)
    assert largest_smallest_integers([5]) == (None, 5)
    assert largest_smallest_integers([-5]) == (-5, None)
    assert largest_smallest_integers([-2, -2, 2, 2]) == (-2, 2)

