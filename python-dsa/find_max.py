"""
Script Name : binary_search.py
Description : Find maximum element in an array
Author      : @tonybnya
"""


def find(nums: list[int]) -> int:
    """
    Find maximum element in an array.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not nums:
        raise ValueError('List is empty')

    maximum: int = nums[0]
    i: int = 1
    while i < len(nums):
        maximum = max(maximum, nums[i])
        i += 1
    return maximum
