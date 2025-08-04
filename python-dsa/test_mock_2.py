"""
Script Name : test_mock_2.py
Description : Set of tests for mock interview 2
Author      : @tonybnya
"""
from mock_2 import RandomizedCollection


def test_insert_and_get_random():
    rc = RandomizedCollection()
    assert rc.insert(10) is True
    assert rc.insert(20) is True
    assert rc.insert(10) is False
    assert rc.insert(30) is True
    assert rc.insert(20) is False

    # Ensure values are in the list
    for _ in range(100):
        assert rc.get_random() in {10, 20, 30}


def test_remove_existing_and_non_existing():
    rc = RandomizedCollection()
    rc.insert(1)
    rc.insert(1)
    rc.insert(2)

    assert rc.remove(1) is True
    assert rc.remove(1) is True
    assert rc.remove(1) is False
    assert rc.remove(2) is True
    assert rc.remove(2) is False


def test_random_distribution():
    rc = RandomizedCollection()
    rc.insert(7)
    rc.insert(7)
    rc.insert(3)

    results = [rc.get_random() for _ in range(1000)]
    assert all(x in [7, 3] for x in results)

    # Check that 7 appears more often than 3
    count_7 = results.count(7)
    count_3 = results.count(3)
    assert count_7 > count_3


def test_all_operations_in_sequence():
    rc = RandomizedCollection()
    assert rc.insert(1) is True
    assert rc.insert(2) is True
    assert rc.insert(1) is False
    assert rc.remove(1) is True
    assert rc.get_random() in [1, 2]
    assert rc.remove(1) is True
    assert rc.remove(1) is False
    assert rc.get_random() == 2
