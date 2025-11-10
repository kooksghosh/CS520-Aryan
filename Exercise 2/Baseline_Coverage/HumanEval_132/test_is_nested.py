import pytest
from is_nested import is_nested

def test_true_cases():
    assert is_nested("[[]]") is True
    assert is_nested("[][[]]") is True
    assert is_nested("][][[]][") is True
    assert is_nested("[[]][") is True

def test_false_cases():
    assert is_nested("[]") is False
    assert is_nested("[][]") is False
    assert is_nested("[[[]") is False
    assert is_nested("]]][[[") is False

