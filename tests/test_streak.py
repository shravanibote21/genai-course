import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_multiple_streaks():
    """Test a list with multiple positive streaks."""
    assert longest_positive_streak([1, 2, 0, 4, 5, 6, -1, 8, 9]) == 3

def test_zeros_and_negatives():
    """Test that zeros and negative numbers break the streak."""
    assert longest_positive_streak([1, 2, 0, 3, -4, 5, 6, 7]) == 3

def test_single_long_streak():
    """Test a single long streak."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_no_positive_numbers():
    """Test a list with no positive numbers."""
    assert longest_positive_streak([0, -1, -2, -3]) == 0

def test_streak_at_the_end():
    """Test a list where the longest streak is at the end."""
    assert longest_positive_streak([-1, 0, 1, 2, 3, 4]) == 4

def test_all_zeros():
    """Test a list of all zeros."""
    assert longest_positive_streak([0, 0, 0, 0]) == 0