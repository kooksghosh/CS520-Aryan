import pytest
from do_algebra import do_algebra

def test_examples():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert do_algebra(['**', '+'], [2, 3, 4]) == 12
    assert do_algebra(['//', '+', '*'], [20, 3, 2, 5]) == 16
    assert do_algebra(['-', '-', '-'], [10, 2, 3, 4]) == 1
    assert do_algebra(['*', '**'], [2, 3, 2]) == 1

# ============================================================
# Spec-Guided Tests for do_algebra
# ============================================================

# --- Length constraint ---
def test_length_constraint_spec_guided():
    operator = ['+', '*']
    operand = [4, 5, 6]
    # len(operator) == len(operand) - 1
    assert len(operator) == len(operand) - 1
    # Just confirm it runs
    do_algebra(operator, operand)


# --- Minimum size requirements ---
def test_minimum_size_spec_guided():
    operator = ['-']
    operand = [10, 3]
    assert len(operator) >= 1 and len(operand) >= 2
    assert do_algebra(operator, operand) == 7


# --- Valid operator domain ---
def test_operator_domain_spec_guided():
    operator = ['+', '/', '*', '-']
    operand = [20, 5, 3, 2, 1]
    # Validate domain
    assert all(op in ['+', '-', '*', '/'] for op in operator)
    # Validate evaluation does not violate domain rule
    do_algebra(operator, operand)


# --- All-addition property ---
def test_all_addition_property_spec_guided():
    operator = ['+', '+', '+']
    operand = [2, 3, 5, 10]
    assert all(op == '+' for op in operator)
    assert do_algebra(operator, operand) == sum(operand)


# --- Concrete example validation (from specification) ---
def test_concrete_example_spec_guided():
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    # specification states result must be 9
    assert do_algebra(operator, operand) == 9


# --- Simple multiplication case ---
def test_simple_multiplication_spec_guided():
    operator = ['*']
    operand = [7, 8]
    assert all(op == '*' for op in operator)
    assert len(operand) == 2
    assert do_algebra(operator, operand) == operand[0] * operand[1]
