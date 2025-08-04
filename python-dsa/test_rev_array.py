"""
Script Name : test_rev_array.py
Description : Set of tests for Reverse Array In-place algorithm
Author      : @tonybnya
"""
import pytest

from rev_array import rev


@pytest.mark.parametrize(
    "nums, expected",
    [
        # Basic cases
        ([1, 2, 3], [3, 2, 1]),
        ([4, 5, 6, 7], [7, 6, 5, 4]),

        # Edge cases
        ([], []),                  # Empty list
        ([42], [42]),             # Single element

        # Duplicates
        ([1, 2, 2, 3], [3, 2, 2, 1]),
        ([7, 7, 7], [7, 7, 7]),

        # Negative numbers
        ([-1, -2, -3], [-3, -2, -1]),

        # Mixed values
        ([0, 1, -1], [-1, 1, 0]),

        # Already reversed
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ]
)
def test_rev_array(nums: list[int], expected: list[int]) -> None:
    """
    Tests.
    """
    assert rev(nums) == expected
