"""
Script Name : mock_2.py
Description : Mock Interview 2
Author      : @tonybnya

Design a class RandomizedCollection with 3 operations, all in O(1) time:

1. insert(val) → add value (accept duplicates)
2. remove(val) → remove value if present
3. get_random() → return random value from current set, uniformly
"""
import random
from collections import defaultdict


class RandomizedCollection:
    """
    Definition of the class.
    """
    def __init__(self):
        """
        Initialize our custom data structure.
        """
        self.lst = []
        self.hmap = defaultdict(set)

    def insert(self, val: int) -> bool:
        """
        Insert a value in our custom data structure.
        """
        is_new: bool = val not in self.hmap
        self.lst.append(val)
        self.hmap[val].add(len(self.lst) - 1)
        return is_new

    def remove(self, val: int) -> bool:
        """
        Remove a value in our custom data structure.
        """
        if val not in self.hmap or not self.hmap[val]:
            return False

        # get any index of val to remove
        idx = self.hmap[val].pop()
        last_element = self.lst[-1]

        # move last_element into the place of idx
        # if they're not the same
        self.lst[idx] = last_element
        self.hmap[last_element].add(idx)
        self.hmap[last_element].discard(len(self.lst) - 1)

        # remove last_element from the list
        self.lst.pop()

        # cleanup the empty set
        if not self.hmap[val]:
            del self.hmap[val]

        return True

    def get_random(self) -> int:
        """
        Get a random element from our custom data structure.
        """
        return random.choice(self.lst)
