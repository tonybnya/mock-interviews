"""
Script Name : mock_1.py
Description : Mock Interview 1
Author      : @tonybnya

Design a class RandomizedSet with 3 operations, all in O(1) time:

1. insert(val) → add value if not present
2. remove(val) → remove value if present
3. get_random() → return random value from current set, uniformly
"""
import random


class RandomizedSet:
    """
    Definition of the class.
    """
    def __init__(self):
        """
        Initialize our custom data structure.
        """
        self.hmap = {}
        self.lst = []

    def insert(self, val: int) -> bool:
        """
        Insert a value in our custom data structure.
        """
        if val in self.hmap:
            return False

        self.hmap[val] = len(self.lst)
        self.lst.append(val)

        return True

    def remove(self, val: int) -> bool:
        """
        Remove a value in our custom data structure.
        """
        if val not in self.hmap:
            return False

        if val != self.lst[-1]:
            idx: int = self.hmap[val]
            last_element: int = self.lst[-1]
            self.lst[idx] = last_element
            self.hmap[last_element] = idx

        self.lst.pop()
        del self.hmap[val]

        return True

    def get_random(self) -> int:
        """
        Get a random value from our custom data structure.
        """
        return random.choice(self.lst)
