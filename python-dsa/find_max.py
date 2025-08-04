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

    # define a variable to hold the first element as the max
    maximum: int = nums[0]

    # loop from the second element to the last
    i: int = 1
    while i < len(nums):
        # set maximum with the new max
        maximum = max(maximum, nums[i])
        i += 1
    return maximum
