"""
Script Name : test_find_max.py
Description : Set of tests for Find maximum algorithm
Author      : @tonybnya
"""
import pytest

from find_max import find


@pytest.mark.parametrize(
    "nums, expected",
    [
        # Basic cases
        ([1, 2, 3, 4, 5], 5),
        ([5, 4, 3, 2, 1], 5),
        ([3, 1, 4, 1, 5, 9], 9),

        # Edge cases
        ([7], 7),                       # Single element
        ([-3, -2, -1], -1),             # All negative
        ([0, -1, -2, -3], 0),           # Zero and negatives

        # Duplicates
        ([2, 2, 2, 2], 2),
        ([1, 2, 3, 3, 3], 3),

        # Large values
        ([999999, 1000000, 888888], 1000000),
    ]
)
def test_find_max(nums: list[int], expected: int) -> None:
    """
    Tests.
    """
    assert find(nums) == expected


def test_find_max_empty():
    """
    Test for empty list (should raise ValueError).
    """
    with pytest.raises(ValueError, match="List is empty"):
        find([])
