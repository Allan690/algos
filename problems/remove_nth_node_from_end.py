"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.



Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]


Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

Follow up: Could you do this in one pass?
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def length(head: ListNode):
    curr = head
    count = 0
    while curr:
        count +=1
        curr = curr.next
    return count


class Solution:
    def removeNthFromEnd_optimal(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        soln: using fast, slow pointer
        the fast pointer gets a headstart to run to n, if getting to n the fast pointer is null, then n is same length
        as list, therefore our first node is target node. therefore, we can return head.next
        else then start to move together while fast.next is true,
        stitch it together: slow.next = slow.next.next
        """
        fast, slow = head, head
        for _ in range(n):
            fast = fast.next
        
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


    def removeNthFromEnd_suboptimal(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        bf: to remove nth node, requires first traversing the list to the end to determine it's length
        index to remove , is going to be n-1
        """
        list_length = length(head) #5
        index_to_remove = list_length - n #3
        if index_to_remove == 0:
            return head.next
        curr = head
        i = 0
        while curr and i != index_to_remove - 1:
            i +=1
            curr = curr.next
        if i == index_to_remove - 1:
            if index_to_remove == list_length - 1:
                curr.next = None
            else:
                curr.next = curr.next.next
        return head
