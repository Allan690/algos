import unittest
from doubly_linked_lists import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):
    def test_insert_head_in_empty_list(self):
        dll = DoublyLinkedList()
        dll.insert_head(10)
        self.assertEqual(dll.head.data, 10)
        self.assertIsNone(dll.head.prev)
        self.assertIsNone(dll.head.next)
        self.assertEqual(dll.head, dll.tail)

    def test_insert_head_in_non_empty_list(self):
        dll = DoublyLinkedList()
        dll.insert_head(10)
        dll.insert_head(20)
        self.assertEqual(dll.head.data, 20)
        self.assertIsNone(dll.head.prev)
        self.assertEqual(dll.head.next.data, 10)
        self.assertEqual(dll.head.next.prev, dll.head)
        self.assertEqual(dll.head.next, dll.tail)

    def test_insert_multiple_heads(self):
        dll = DoublyLinkedList()
        dll.insert_head(10)
        dll.insert_head(20)
        dll.insert_head(30)
        self.assertEqual(dll.head.data, 30)
        self.assertEqual(dll.head.next.data, 20)
        self.assertEqual(dll.head.next.next.data, 10)
        self.assertEqual(dll.head.next.next, dll.tail)

    def test_insert_tail_in_empty_list(self):
        dll = DoublyLinkedList()
        dll.insert_tail(10)
        self.assertEqual(dll.tail.data, 10)
        self.assertIsNone(dll.tail.prev)
        self.assertIsNone(dll.tail.next)
        self.assertEqual(dll.head, dll.tail)

    def test_insert_tail_in_non_empty_list(self):
        dll = DoublyLinkedList()
        dll.insert_head(10)
        dll.insert_tail(20)
        self.assertEqual(dll.tail.data, 20)
        self.assertEqual(dll.head.data, 10)
        self.assertEqual(dll.tail.prev.data, 10)
        self.assertIsNone(dll.tail.next)
        self.assertIsNone(dll.head.prev)
        self.assertEqual(dll.head.next, dll.tail)

    def test_insert_multiple_tails(self):
            dll = DoublyLinkedList()
            dll.insert_tail(10)
            dll.insert_tail(20)
            dll.insert_tail(30)
            self.assertEqual(dll.tail.data, 30)
            self.assertEqual(dll.tail.prev.data, 20)
            self.assertEqual(dll.tail.prev.prev.data, 10)
            self.assertEqual(dll.head.data, 10)

    def test_insert_middle_in_empty_list(self):
        dll = DoublyLinkedList()
        dll.insert_middle(10)
        self.assertEqual(dll.head.data, 10)
        self.assertIsNone(dll.head.prev)
        self.assertIsNone(dll.head.next)
        self.assertEqual(dll.head, dll.tail)

    def test_insert_middle_in_odd_list(self):
        dll = DoublyLinkedList()
        for data in [10, 30]:
            dll.insert_tail(data)
        dll.insert_middle(20)
        self.assertEqual(dll.head.next.data, 20)
        self.assertEqual(dll.head.next.next.data, 30)
        self.assertEqual(dll.head.next.prev.data, 10)
        self.assertEqual(dll.tail.data, 30)

    def test_insert_middle_in_even_list(self):
        dll = DoublyLinkedList()
        for data in [10, 20, 40]:
            dll.insert_tail(data)
        dll.insert_middle(30)
        self.assertEqual(dll.head.next.next.data, 30)
        self.assertEqual(dll.head.next.next.next.data, 40)
        self.assertEqual(dll.head.next.next.prev.data, 20)
        self.assertEqual(dll.tail.data, 40)

    def test_insert_at_index_beginning(self):
        dll = DoublyLinkedList()
        for data in [20, 30]:
            dll.insert_tail(data)
        dll.insert_at_index(0, 10)
        self.assertEqual(dll.head.data, 10)
        self.assertEqual(dll.head.next.data, 20)

    def test_insert_at_index_end(self):
        dll = DoublyLinkedList()
        for data in [10, 20]:
            dll.insert_tail(data)
        dll.insert_at_index(2, 30)  # Assuming 0-based indexing
        self.assertEqual(dll.tail.data, 30)
        self.assertEqual(dll.tail.prev.data, 20)

    def test_insert_at_index_middle(self):
        dll = DoublyLinkedList()
        for data in [10, 30]:
            dll.insert_tail(data)
        dll.insert_at_index(1, 20)
        self.assertEqual(dll.head.next.data, 20)
        self.assertEqual(dll.head.next.next.data, 30)

    def test_insert_at_index_in_empty_list(self):
        dll = DoublyLinkedList()
        dll.insert_at_index(0, 10)
        self.assertEqual(dll.head.data, 10)
        self.assertIsNone(dll.head.prev)
        self.assertIsNone(dll.head.next)

    def test_insert_at_index_out_of_bounds(self):
        dll = DoublyLinkedList()
        dll.insert_tail(10)
        with self.assertRaises(IndexError):
            dll.insert_at_index(2, 20)  # Index out of range

if __name__ == "__main__":
    unittest.main()
