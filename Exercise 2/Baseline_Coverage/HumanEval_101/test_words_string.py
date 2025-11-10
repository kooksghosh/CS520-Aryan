import pytest
from words_string import words_string

def test_examples():
    assert words_string('one,two,three') == ['one', 'two', 'three']
    assert words_string('one two three') == ['one', 'two', 'three']
    assert words_string('one, two,  three') == ['one', 'two', 'three']
    assert words_string('  alpha,beta , gamma') == ['alpha', 'beta', 'gamma']
    assert words_string('word') == ['word']

