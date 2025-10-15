import pytest
from streak import longest_positive_streak

def test_empty_list():
    assert longest_positive_streak([]) == 0

def test_multiple_streaks():
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_with_zeros_and_negatives():
    assert longest_positive_streak([-1, -2, 0, -3]) == 0
    assert longest_positive_streak([1, 2, 0, 3, 4, 5, -1, 6]) == 3

def test_all_positive():
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_single_element_list():
    assert longest_positive_streak([1]) == 1
    assert longest_positive_streak([-1]) == 0
    assert longest_positive_streak([0]) == 0

def test_streaks_at_beginning_and_end():
    assert longest_positive_streak([1, 2, 3, -5, 4]) == 3
    assert longest_positive_streak([-1, 2, 3, 4, 5]) == 4

def test_identical_positive_numbers():
    assert longest_positive_streak([1, 1, 1]) == 3