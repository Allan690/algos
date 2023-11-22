import unittest
from datastructures.doubly_linked_lists import DoublyLinkedList


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

    def test_delete_at_index_empty_list(self):
        dll = DoublyLinkedList()
        with self.assertRaises(IndexError):
            dll.delete_at_index(0)

    def test_delete_at_start(self):
        # Setup the list with some elements
        dll = DoublyLinkedList()
        dll.insert_head(2)
        dll.insert_head(1)
        dll.delete_at_index(0)
        self.assertEqual(len(dll), 1)
        self.assertEqual(dll.head.data, 2)

    def test_delete_at_middle(self):
        dll = DoublyLinkedList()
        for data in [1, 2, 3]:
            dll.insert_head(data)
        dll.delete_at_index(1)
        self.assertEqual(len(dll), 2)
        self.assertEqual(dll.head.data, 3)
        self.assertEqual(dll.head.next.data, 1)
        self.assertEqual(dll.head.next.prev.data, 3)

    def test_delete_at_end(self):
        dll = DoublyLinkedList()
        for data in [1, 2, 3]:
            dll.insert_head(data)
        dll.delete_at_index(2)
        self.assertEqual(len(dll), 2)
        self.assertEqual(dll.head.data, 3)
        self.assertEqual(dll.head.next.data, 2)
        self.assertIsNone(dll.head.next.next)

    def test_delete_at_invalid_index(self):
        dll = DoublyLinkedList()
        dll.insert_head(1)
        with self.assertRaises(IndexError):
            dll.delete_at_index(2)

    def test_delete_head_empty_list(self):
        dll = DoublyLinkedList()
        self.assertIsNone(dll.delete_at_head())

    def test_delete_head_single_element(self):
        dll = DoublyLinkedList()
        dll.insert_head(10)
        self.assertIsNone(dll.delete_at_head())
        self.assertIsNone(dll.head)
        self.assertIsNone(dll.tail)

    def test_delete_head_multiple_elements(self):
        dll = DoublyLinkedList()
        dll.insert_tail(10)
        dll.insert_tail(20)
        dll.insert_tail(30)
        self.assertEqual(dll.delete_at_head().data, 20)
        self.assertEqual(dll.head.data, 20)
        self.assertIsNone(dll.head.prev)
        self.assertEqual(dll.head.next.data, 30)

    def test_delete_tail_empty_list(self):
        dll = DoublyLinkedList()
        self.assertIsNone(dll.delete_at_tail())

    def test_delete_tail_single_element(self):
        dll = DoublyLinkedList()
        dll.insert_head(10)
        self.assertIsNone(dll.delete_at_tail())
        self.assertIsNone(dll.head)
        self.assertIsNone(dll.tail)

    def test_delete_tail_multiple_elements(self):
        dll = DoublyLinkedList()
        dll.insert_tail(10)
        dll.insert_tail(20)
        dll.insert_tail(30)
        self.assertEqual(dll.delete_at_tail().data, 10)
        self.assertEqual(dll.tail.data, 20)
        self.assertIsNone(dll.tail.next)
        self.assertEqual(dll.tail.prev.data, 10)


if __name__ == "__main__":
    unittest.main()
