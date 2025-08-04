"""
Script Name : rev_array.py
Description : Reverse an array in-place
Author      : @tonybnya
"""


def rev(nums: list[int]) -> list[int]:
    """
    Reverse array in-place
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        # swap elements at the two pointers
        nums[left], nums[right] = nums[right], nums[left]
        # increment left
        left += 1
        # decrement right
        right -= 1
    return nums
