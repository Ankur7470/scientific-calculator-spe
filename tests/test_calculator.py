import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  
import pytest
from calculator_functions import square_root, factorial, natural_log, power

def test_square_root():
    assert square_root(4) == 2
    assert round(square_root(2), 3) == 1.414

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1

def test_natural_log():
    assert round(natural_log(1), 3) == 0.000
    assert round(natural_log(2.71828), 3) == 1.000

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1


