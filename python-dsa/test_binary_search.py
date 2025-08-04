"""
Script Name : test_binary_search.py
Description : Set of tests for Binary Search algorithm
Author      : @tonybnya
"""
import pytest

from binary_search import search


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        # Basic cases
        ([1, 2, 3, 4, 5], 3, True),
        ([1, 2, 3, 4, 5], 6, False),

        # Edge cases
        ([], 1, False),                   # Empty list
        ([1], 1, True),                   # One element, match
        ([1], 2, False),                  # One element, no match

        # Duplicates (binary search still works but may not find first/last occurrence)
        ([1, 2, 2, 2, 3], 2, True),
        ([1, 1, 1, 1], 2, False),

        # Negative numbers
        ([-10, -5, -2, 0, 3], -5, True),
        ([-10, -5, -2, 0, 3], 4, False),

        # Target at boundaries
        ([10, 20, 30, 40], 10, True),     # First element
        ([10, 20, 30, 40], 40, True),     # Last element

        # Large list
        (list(range(0, 100000, 2)), 44444, True),     # Exists
        (list(range(0, 100000, 2)), 44445, False),    # Does not exist
    ]
)
def test_binary_search(nums: list[int], target: int, expected: bool) -> None:
    """
    Tests for Binary Search algorithm.
    """
    assert search(nums, target) == expected
