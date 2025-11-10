import pytest
from do_algebra import do_algebra

def test_examples():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert do_algebra(['**', '+'], [2, 3, 4]) == 12
    assert do_algebra(['//', '+', '*'], [20, 3, 2, 5]) == 16
    assert do_algebra(['-', '-', '-'], [10, 2, 3, 4]) == 1
    assert do_algebra(['*', '**'], [2, 3, 2]) == 18

#Assisted Test Cases Generation
def test_unsupported_operator_raises_value_error():
    # Includes an operator not in the allowed set
    with pytest.raises(ValueError) as excinfo:
        do_algebra(['+', '@', '-'], [1, 2, 3, 4])
    assert "unsupported operator" in str(excinfo.value)


def test_len_mismatch_raises_value_error():
    # Mismatch: need len(operand) - 1 operators; here it's too few
    with pytest.raises(ValueError) as excinfo:
        do_algebra(['+', '-'], [1, 2, 3, 4])  # expects 3 operators
    assert "len(operator) must be len(operand) - 1" in str(excinfo.value)
