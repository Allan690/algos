import unittest

from problems.lru_cache import LRUCache

class TestLRUCache(unittest.TestCase):
    def test_cache_initialization(self):
        cache = LRUCache(2)
        self.assertEqual(cache.get(1), -1, "Cache should return -1 for non-existent key")

    def test_put_and_get(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1, "Cache should return 1 for key 1")
        self.assertEqual(cache.get(2), 2, "Cache should return 2 for key 2")

    def test_update_existing_key(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(1, 10)
        self.assertEqual(cache.get(1), 10, "Cache should update existing key")

    def test_evict_lru(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(3, 3)  # This should evict key 1
        self.assertEqual(cache.get(1), -1, "Cache should evict the least recently used item")
    
    def test_recently_used_after_get(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1, "Cache should return 1 for key 1")
        cache.put(3, 3)  # This should evict key 2, not key 1
        self.assertEqual(cache.get(2), -1, "Cache should evict key 2, not key 1")
        self.assertEqual(cache.get(1), 1, "Cache should still have key 1")

    def test_capacity_limit(self):
        cache = LRUCache(1)
        cache.put(1, 1)
        cache.put(2, 2)  # This should evict key 1
        self.assertEqual(cache.get(1), -1, "Cache should adhere to its capacity")
