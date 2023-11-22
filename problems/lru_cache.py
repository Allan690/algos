"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.



Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4


Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
"""

class Node:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity) -> None:
        self.cap = capacity
        self.m = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node(self, node):
        """
        adds a node to the linked list(cache) after the header of the list
        requires storing the reference to the next of the header
        """
        header_next = self.head.next
        node.next = header_next
        node.prev = self.head
        header_next.prev = node
        self.head.next = node

    def remove_node(self, node):
        """
        removes a node from the linked list.
        requires storing a reference to the next node to the node we want to delete
        """
        next_node_after_desired = node.next
        prev_node_before_desired = node.prev
        prev_node_before_desired.next = next_node_after_desired
        next_node_after_desired.prev = prev_node_before_desired


    def get(self, key: int) -> int:
        """
        when getting an item,
        we first check if the item exists in the map, if not return -1
        if so, we retrieve the item(node reference) in the map by the key
        we then store the value of the node in a variable to be returned to the caller
        we then delete the node in the linked list, and the key in the map
        we then add back the node to the linked list(this brings it to the head of the LL(MRU))
        we then add the key back to the map with a reference to self.head.next(MRU node)
        """
        if not key in self.m:
            return -1
        node = self.m[key]
        val = node.val
        self.remove_node(node)
        del self.m[key]
        self.add_node(node)
        self.m[key] = self.head.next
        return val

    def put(self, key: int, value: int) -> None:
        """
        when updating an item, do the following
        we first check if the item exists in the map, if so, we retrieve the value(node reference) and store the val
        we then delete the node and the key in the map
        we then check if the size of the map is equal to the allowed capacity, if so, remove the LRU item from map and list
        the LRU node will be self.tail.prev, key will be self.tail.prev.key
        add node to list
        add key to map
        """
        if key in self.m:
            node = self.m[key]
            self.remove_node(node)
            del self.m[key]
        if len(self.m) == self.cap:
            # delete lru node
            last_node_key = self.tail.prev.key
            self.remove_node(self.tail.prev)
            del self.m[last_node_key]
        # add node
        self.add_node(Node(key, value))
        self.m[key] = self.head.next
