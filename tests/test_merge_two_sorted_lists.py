import unittest
from problems.merge_two_sorted_lists import ListNode, Solution


def list_to_linkedlist(lst):
    head = ListNode()
    current = head
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return head.next

def linkedlist_to_list(node):
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst

class TestMergeTwoLists(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        list1 = list_to_linkedlist([1,2,4])
        list2 = list_to_linkedlist([1,3,4])
        merged = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(linkedlist_to_list(merged), [1,1,2,3,4,4])

    def test_example_2(self):
        list1 = list_to_linkedlist([])
        list2 = list_to_linkedlist([])
        merged = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(linkedlist_to_list(merged), [])

    def test_example_3(self):
        list1 = list_to_linkedlist([])
        list2 = list_to_linkedlist([0])
        merged = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(linkedlist_to_list(merged), [0])

    # Additional test cases
    def test_empty_and_non_empty(self):
        list1 = list_to_linkedlist([1,2,3])
        list2 = list_to_linkedlist([])
        merged = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(linkedlist_to_list(merged), [1,2,3])

    def test_non_empty_and_empty(self):
        list1 = list_to_linkedlist([])
        list2 = list_to_linkedlist([4,5,6])
        merged = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(linkedlist_to_list(merged), [4,5,6])

    def test_single_element_lists(self):
        list1 = list_to_linkedlist([1])
        list2 = list_to_linkedlist([2])
        merged = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(linkedlist_to_list(merged), [1,2])
