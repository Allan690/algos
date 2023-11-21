import unittest

from problems.remove_linked_list_elements import ListNode, Solution

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


class TestRemoveElements(unittest.TestCase):

    def setUp(self):
        # Setup the Solution object
        self.solution = Solution()

    def test_remove_middle_elements(self):
        head = array_to_linkedlist([1, 2, 6, 3, 4, 5, 6])
        result = self.solution.removeElements(head, 6)
        self.assertEqual(linkedlist_to_array(result), [1, 2, 3, 4, 5])

    def test_remove_head_elements(self):
        head = array_to_linkedlist([6, 1, 2, 3, 4, 5])
        result = self.solution.removeElements(head, 6)
        self.assertEqual(linkedlist_to_array(result), [1, 2, 3, 4, 5])

    def test_empty_list(self):
        head = array_to_linkedlist([])
        result = self.solution.removeElements(head, 1)
        self.assertIsNone(result)

    def test_all_elements_removed(self):
        head = array_to_linkedlist([7, 7, 7, 7])
        result = self.solution.removeElements(head, 7)
        self.assertIsNone(result)

    def test_very_long_list(self):
        long_list = [1] * 1000 + [2] * 1000
        head = array_to_linkedlist(long_list)
        result = self.solution.removeElements(head, 1)
        self.assertEqual(linkedlist_to_array(result), [2] * 1000)

    def test_list_with_repeated_elements(self):
        head = array_to_linkedlist([1, 1, 1, 1, 1])
        result = self.solution.removeElements(head, 1)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
