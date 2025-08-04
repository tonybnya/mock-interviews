"""
Script Name : test_linear_search.py
Description : Set of tests for Linear Search algorithm
Author      : @tonybnya
"""
import pytest

from linear_search import search


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        # Basic cases
        ([1, 2, 3, 4, 5], 3, True),
        ([1, 2, 3, 4, 5], 6, False),

        # Edge cases
        ([], 1, False),                          # Empty list
        ([1], 1, True),                          # Single-element, match
        ([1], 2, False),                         # Single-element, no match

        # Duplicates
        ([1, 2, 2, 3], 2, True),
        ([1, 1, 1, 1], 2, False),

        # Negative numbers
        ([-5, -3, -1, 0], -3, True),
        ([-5, -3, -1, 0], 2, False),

        # Large list
        (list(range(10_000)), 9999, True),
        (list(range(10_000)), 10_000, False),

        # Target at the start and end
        ([9, 1, 2, 3], 9, True),
        ([1, 2, 3, 4], 4, True),
    ]
)
def test_linear_search(nums: list[int], target: int, expected: bool) -> None:
    """
    Tests for Linear Search algorithm.
    """
    assert search(nums, target) == expected
