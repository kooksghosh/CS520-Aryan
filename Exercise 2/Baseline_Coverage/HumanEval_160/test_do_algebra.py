import pytest
from do_algebra import do_algebra

def test_examples():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert do_algebra(['**', '+'], [2, 3, 4]) == 12
    assert do_algebra(['//', '+', '*'], [20, 3, 2, 5]) == 16
    assert do_algebra(['-', '-', '-'], [10, 2, 3, 4]) == 1
    assert do_algebra(['*', '**'], [2, 3, 2]) == 18
