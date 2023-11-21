from problems.merge_k_sorted_lists import ListNode, Solution


def array_to_linkedlist(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def linkedlist_to_array(head):
    arr = []
    current = head
    while current:
        arr.append(current.val)
        current = current.next
    return arr


import unittest

class TestMergeKLists(unittest.TestCase):

    def setUp(self):
        # Setup the Solution object
        self.solution = Solution()

    def test_merge_multiple_lists(self):
        # Testing merging multiple sorted linked lists
        lists = [
            array_to_linkedlist([1, 4, 5]),
            array_to_linkedlist([1, 3, 4]),
            array_to_linkedlist([2, 6])
        ]
        merged = self.solution.mergeKLists(lists)
        self.assertEqual(linkedlist_to_array(merged), [1, 1, 2, 3, 4, 4, 5, 6])

    def test_empty_lists(self):
        # Testing merging empty lists
        lists = []
        merged = self.solution.mergeKLists(lists)
        self.assertIsNone(merged)

    def test_lists_with_empty_list(self):
        # Testing merging lists that include an empty list
        lists = [array_to_linkedlist([1, 2, 3]), None]
        merged = self.solution.mergeKLists(lists)
        self.assertEqual(linkedlist_to_array(merged), [1, 2, 3])

    def test_single_list(self):
        # Testing merging a single list
        lists = [array_to_linkedlist([1, 2, 3])]
        merged = self.solution.mergeKLists(lists)
        self.assertEqual(linkedlist_to_array(merged), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
