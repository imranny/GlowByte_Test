import pytest
from task2 import merge_digit_intervals

def test_1():
    assert merge_digit_intervals([]) == []

def test_2():
    assert merge_digit_intervals([[1, 3]]) == [[1, 3]]

def test_3():
    assert merge_digit_intervals([[1, 3], [4, 6]]) == [[1, 3], [4, 6]]

def test_4():
    assert merge_digit_intervals([[1, 5], [2, 3]]) == [[1, 5]]

def test_5():
    assert merge_digit_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]