"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []


Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
"""
# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def merge_two_sorted_lists(self, lsts):
        lst_node = ListNode()

        dummy = lst_node

        lst1, lst2 = lsts[0], lsts[1]

        while lst1 and lst2:
            if lst1.val < lst2.val:
                dummy.next = lst1
                lst1 = lst1.next
            else:
                dummy.next = lst2
                lst2 = lst2.next
            dummy = dummy.next
        dummy.next = lst1 or lst2
        return lst_node.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 2:
            return self.merge_two_sorted_lists(lists)
        else:
            first_two = lists[:2]
            merged = self.merge_two_sorted_lists(first_two)
            for lst in lists[2:]:
                merged = self.merge_two_sorted_lists([merged, lst])
            return merged
