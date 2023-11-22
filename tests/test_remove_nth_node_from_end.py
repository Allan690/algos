import unittest

from problems.remove_nth_node_from_end import ListNode, Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def list_to_array(self, head):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return arr

    def array_to_list(self, arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for value in arr[1:]:
            current.next = ListNode(value)
            current = current.next
        return head

    def test_remove_nth_from_end_single_node(self):
        head = self.array_to_list([1])
        new_head = self.solution.removeNthFromEnd_optimal(head, 1)
        new_head_2 = self.solution.removeNthFromEnd_suboptimal(head, 1)
        self.assertIsNone(new_head)
        self.assertIsNone(new_head_2)

    def test_remove_nth_from_end_multiple_nodes_middle(self):
        head = self.array_to_list([1, 2, 3, 4, 5])
        new_head = self.solution.removeNthFromEnd_optimal(head, 2)
        self.assertEqual(self.list_to_array(new_head), [1, 2, 3, 5])
        new_head_2 = self.solution.removeNthFromEnd_suboptimal(
            self.array_to_list([1, 2, 3, 4, 5]), 2
        )
        self.assertEqual(self.list_to_array(new_head_2), [1, 2, 3, 5])

    def test_remove_nth_from_end_multiple_nodes_head(self):
        head = self.array_to_list([1, 2])
        new_head = self.solution.removeNthFromEnd_optimal(head, 2)
        new_head_2 = self.solution.removeNthFromEnd_suboptimal(
            self.array_to_list([1, 2]), 2
        )
        self.assertEqual(self.list_to_array(new_head), [2])
        self.assertEqual(self.list_to_array(new_head_2), [2])

    def test_remove_nth_from_end_multiple_nodes_tail(self):
        head = self.array_to_list([1, 2, 3])
        new_head = self.solution.removeNthFromEnd_optimal(head, 1)
        new_head_2 = self.solution.removeNthFromEnd_suboptimal(
            self.array_to_list([1, 2, 3]), 1
        )
        self.assertEqual(self.list_to_array(new_head), [1, 2])
        self.assertEqual(self.list_to_array(new_head_2), [1, 2])


if __name__ == "__main__":
    unittest.main()
