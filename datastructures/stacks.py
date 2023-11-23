"""
The stack is a fundamental ds , noted for it's LIFO (Last in first out) principle i.e
last item added to the stack is the first element to be removed.

operations:
- push - add item to the top of the stack => O(1)
- pop - remove item at the top of the stack -  O(1)
- peek/top -> view top item of the stack without removing it  O(1)
- isEmpty - check if the stack is empty  O(1)
- search - finding an element in the stack - O(1)
- size - getting the size of the stack - O(1)

Implementation
- stacks can be implemented with either fixed/dynamic arrays or with linked lists

1. Using arrays
-> pushing involves adding an element at the next available index
-> popping involves removing the element at the last index
simple but inefficient, if array needs to be resized constantly.


2. Using linked lists
-> each element is a node with a reference to the next node
-> pushing involves adding a new node at the beginning of the list
-> popping involves removing the first node
 More efficient since it does require contiguous memory allocation.

 Uses
 1. Function calls and recursions -> call stack stores info of active subroutines and functions
 2. Expression evaluation -> used in algorithms for evaluating arithmetic expressions and in converting expressions
 from infix to postfix/prefix notations.
 3. Undo mechanisms -> stacks in software application, can record actions for undo actions.
 4. Backtracking algorithms -> in algorithms where you need to backtrack to a previous state such as in a maze solving
 game.
 5. Syntax parsing -> Compilers and interpreters often use stacks for parsing and validating syntax.
 6. Memory management -> Certain memory allocation strategies use stacks for managing memory.
"""
from abc import abstractmethod, ABC


class StackDS(ABC):
    @abstractmethod
    def push(self, item):
        raise NotImplementedError('push not implemented')

    @abstractmethod
    def pop(self):
        raise NotImplementedError('pop not implemented')

    @abstractmethod
    def peek(self):
        raise NotImplementedError('peek not implemented')

    @abstractmethod
    def isEmpty(self):
        raise NotImplementedError('isEmpty not implemented')

    @abstractmethod
    def search(self):
        raise NotImplementedError('search not implemented')

    @abstractmethod
    def size(self):
        raise NotImplementedError('size not implemented')


class StackArrayImpl(StackDS):
    """
    implements the stack data structure using arrays
    """
    def __init__(self) -> None:
        self.stack = []

    def push(self, item):
        """
        adds an item to the top of the stack, appending it to the array
        """
        self.stack.append(item)


    def pop(self):
        """
        removes the last item in the array -- corresponds to the item at the top of the stack
        """
        return self.stack.pop(len(self.stack) - 1)

    def peek(self):
        """
        gives a view into the item at the top of the stack without deleting it
        """
        return self.stack[-1]

    def isEmpty(self):
        """
        checks if the stack is empty or not, returns true or false
        """
        return len(self.stack) == 0

    def search(self, item):
        """
        searches for an item in the stack
        """
        for ind, value  in enumerate(self.stack):
            if value == item:
                return ind
        return -1

    def size(self):
        """
        returns the size of the stack
        """
        return len(self.stack)


class Node:
    def __init__(self, data, prev=None, next=None) -> None:
        self.val = data
        self.prev = prev
        self.next = next


class StackLinkedListImpl(StackDS):
    def __init__(self) -> None:
        """
        we have the head and tail nodes of our linked list here initiated as sentinels
        """
        self.head = Node(data=-1)
        self.tail = Node(data=-1)
        self.head.next = self.tail
        self.tail.prev = self.head


    def push(self, item):
        """
        adds an item to the top of the stack(head of the linked list)
        """
        new_node = Node(item, prev=self.head, next=self.head.next)
        node_after_head = self.head.next
        self.head.next = new_node
        node_after_head.prev = new_node


    def pop(self):
        """
        removes the item at the top of the stack(head of the linked list)
        """
        if self.head.next == self.tail:
            raise IndexError('list is empty')
        node_to_remove = self.head.next
        node_after_node_to_remove = node_to_remove.next
        node_after_node_to_remove.prev = self.head
        self.head.next = node_after_node_to_remove
        return node_to_remove.val


    def peek(self):
        """
        gives you a view of the item at the top of the stack(head node) but does not remove it
        """
        if self.head.next == self.tail:
            raise IndexError('list is empty')
        return self.head.next.val


    def isEmpty(self):
        """
        checks if the stack is empty or not
        """
        return self.head.next == self.tail


    def search(self, item):
        """
        checks if an item is in the stack - requires traversing the entire list
        """
        curr = self.head.next
        count = 0
        while curr.next != self.tail:
            if curr.val == item:
                return count
            count +=1
            curr = curr.next
        return -1


    def size(self):
        """
        returns the size of the stack
        """
        curr = self.head
        count = 0
        while curr.next != self.tail:
            count +=1
            curr = curr.next
        return count

