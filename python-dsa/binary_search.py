"""
Script Name : binary_search.py
Description : Implement Binary Search algorithm
Author      : @tonybnya
"""


def search(nums: list[int], target: int) -> bool:
    """
    Binary Search algorithm
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid: int = (left + right) // 2
        if nums[mid] == target:
            return True
        if nums[mid] > target:
            right = mid - 1
        if nums[mid] < target:
            left = mid + 1
    return False
