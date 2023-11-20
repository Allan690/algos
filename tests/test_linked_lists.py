import unittest

from linked_lists import LinkedList

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        # Setup for the tests; creating a linked list with some nodes
        self.linkedList = LinkedList()
        self.linkedList.insert_head(1)
        self.linkedList.insert_head(2)
        self.linkedList.insert_head(3)  # LinkedList: 3 -> 2 -> 1

    def test_search(self):
        # Testing the search functionality
        node = self.linkedList.search(2)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 2)
        # Testing for a node not in the list
        with self.assertRaises(ValueError):
            self.linkedList.search(4)

    def test_insert_head(self):
        # Testing insertion at the head
        self.linkedList.insert_head(4)  # LinkedList: 4 -> 3 -> 2 -> 1
        self.assertEqual(self.linkedList.head.data, 4)

    def test_insert_tail(self):
        # Testing insertion at the tail
        self.linkedList.insert_tail(0)  # LinkedList: 3 -> 2 -> 1 -> 0
        self.assertEqual(self.linkedList.tail.data, 0)

    def test_length(self):
        # Testing the length of the linked list
        length = self.linkedList.length()
        self.assertEqual(length, 3)  # Length should be 3

    def test_insert_middle(self):
        # Testing insertion in the middle
        self.linkedList.insert_middle(5)  # LinkedList: 3 -> 5 -> 2 -> 1
        self.assertEqual(self.linkedList.head.next.data, 5)

    def test_delete_at_head(self):
        # Testing deletion at head
        self.linkedList.delete_at_head()  # LinkedList: 3 -> 5 -> 2 -> 1
        self.assertEqual(self.linkedList.head.data, 2)
        self.assertEqual(self.linkedList.length(), 2)
        with self.assertRaises(ValueError):
            self.linkedList.delete_at_head()
            self.linkedList.delete_at_head()
            self.linkedList.delete_at_head()

    def test_delete_at_tail(self):
        self.linkedList.delete_at_tail()
        self.assertEqual(self.linkedList.head.data, 3)
        self.assertEqual(self.linkedList.tail.data, 2)
        self.assertEqual(self.linkedList.length(), 2)
        with self.assertRaises(ValueError):
            self.linkedList.search(1)

if __name__ == '__main__':
    unittest.main()
