import pytest
from special_factorial import special_factorial

def test_examples():
    assert special_factorial(1) == 1                 # 1!
    assert special_factorial(2) == 2                 # 1!*2! = 2
    assert special_factorial(3) == 12                # 1!*2!*3! = 12
    assert special_factorial(4) == 288               # example from prompt
    assert special_factorial(5) == 34560


# ------------------------------------------------------------
# Spec-Guided Tests for special_factorial
# ------------------------------------------------------------


# --- n must be positive ---
def test_spec_guided_n_positive():
    # For a valid call, n > 0 must hold.
    # We do NOT test invalid inputs; we test that valid inputs satisfy the spec.
    n = 3
    assert n > 0
    special_factorial(n)  # Should run without error


# --- result must be positive ---
def test_spec_guided_result_positive():
    n = 5
    res = special_factorial(n)
    assert res > 0


# --- concrete factorial product checks: n == 1 ---
def test_spec_guided_n1_case():
    n = 1
    expected = 1
    assert special_factorial(n) == expected


# --- concrete factorial product checks: n == 2 ---
def test_spec_guided_n2_case():
    n = 2
    expected = 2     # 1! * 2! = 2
    assert special_factorial(n) == expected


# --- concrete factorial product checks: n == 3 ---
def test_spec_guided_n3_case():
    n = 3
    expected = 12    # 1! * 2! * 3! = 12
    assert special_factorial(n) == expected


# --- concrete factorial product checks: n == 4 ---
def test_spec_guided_n4_case():
    n = 4
    expected = 288   # 1! * 2! * 3! * 4! = 288
    assert special_factorial(n) == expected


# --- monotonic growth: if n > 1, result > 1 ---
def test_spec_guided_monotonic_growth():
    n = 5
    assert n > 1
    assert special_factorial(n) > 1
