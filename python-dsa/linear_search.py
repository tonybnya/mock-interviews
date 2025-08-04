"""
Script Name : linear_search.py
Description : Implement Linear Search algorithm
Author      : @tonybnya
"""


def search(nums: list[int], target: int) -> bool:
    """
    Linear Search algorithm
    Time Complexity: O(n)
    space Complexity: O(1)
    """
    for num in nums:
        if num == target:
            return True
    return False
