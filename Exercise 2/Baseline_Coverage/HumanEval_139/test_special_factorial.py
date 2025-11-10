import pytest
from special_factorial import special_factorial

def test_examples():
    assert special_factorial(1) == 1                 # 1!
    assert special_factorial(2) == 2                 # 1!*2! = 2
    assert special_factorial(3) == 12                # 1!*2!*3! = 12
    assert special_factorial(4) == 288               # example from prompt
    assert special_factorial(5) == 34560

