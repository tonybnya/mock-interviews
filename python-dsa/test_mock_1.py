"""
Script Name : test_mock_1.py
Description : Set of tests for mock interview 1
Author      : @tonybnya
"""
from mock_1 import RandomizedSet


def test_insert_unique():
    r = RandomizedSet()
    assert r.insert(10) == True
    assert r.insert(20) == True
    assert r.insert(10) == False


def test_remove_existing_and_absent():
    r = RandomizedSet()
    r.insert(5)
    r.insert(7)
    assert r.remove(5) == True
    assert r.remove(5) == False
    assert r.remove(2) == False


def test_get_random_basic():
    r = RandomizedSet()
    r.insert(1)
    r.insert(2)
    r.insert(3)
    results = set(r.get_random() for _ in range(100))
    assert results.issubset({1, 2, 3})
    assert len(results) >= 2


def test_remove_and_insert_consistency():
    r = RandomizedSet()
    assert r.insert(1)
    assert r.insert(2)
    assert r.remove(1)
    assert r.insert(1)
    assert sorted(r.lst) == sorted(r.hmap.keys())


def test_get_random_after_removal():
    r = RandomizedSet()
    r.insert(100)
    r.insert(200)
    r.remove(100)
    for _ in range(10):
        assert r.get_random() == 200
