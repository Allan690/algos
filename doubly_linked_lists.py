"""
A doubly linked list is a special LL where each node contains a pointer to the previous node, data and a pointer to the
next node.

Adv:
- can be traversed both backwards and forwards
- delete is more efficient if pointer to the node to be deleted is provided
- quick insertions of a new node before a given node


Apps:
- by web browsers for back and forward navigation of web pages
- LRU and MRU caches are constructed using DLLs
- used by various apps to maintain undo and redo functionalities
- In OS, a DLL is used by the thread scheduler to keep track of processes being executed at that time
"""


class Node:
    """
    node has a reference to the previos node, forward node and data
    """

    def __init__(self, prev=None, next=None, data=None) -> None:
        self.prev = prev
        self.next = next
        self.data = data


class DoublyLinkedList:
    def __init__(self, head: Node = None, tail: Node = None) -> None:
        self.head = head
        self.tail = tail

    def __str__(self) -> str:
        stringified = ""
        curr = self.head
        while curr:
            stringified += str(curr.data) + "-->"
            curr = curr.next
        return stringified

    def __len__(self):
        """
        gets the length of the DLL. This requires traversing the entire list keeping count of the nodes
        """
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def insert_head(self, data):
        """
        inserts a node at the head of the linked list. this involves setting current head to next element of the new node,
        setting prev of current head to new node, and setting prev of new node to None
        """
        if self.head is None:
            new_node = Node(prev=None, next=None, data=data)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(prev=None, next=self.head, data=data)
            self.head.prev = new_node
            self.head = new_node

        return self.head

    def insert_tail(self, data):
        """
        inserts a node at the tail of the list. Since we maintain a tail node, this is a constant time operation
        that involves pointing the next of the current tail to the new node, and making the new node's prev curr tail.
        """
        if self.tail is None:
            new_node = Node(prev=None, next=None, data=data)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(prev=self.tail, next=None, data=data)
            self.tail.next = new_node
            self.tail = new_node
        return self.tail

    def insert_middle(self, data):
        """
        insert at the middle of the DLL. This requires determining the length of the list, determining the mid point,
        and inserting data at that point
        """
        dll_length = len(self)
        # in length is even, insert after the (n +1) // 2 node else (n//2) node
        mid = dll_length // 2 if dll_length % 2 == 0 else (dll_length + 1) // 2
        curr = self.head
        if not curr:
            new_node = Node(prev=None, next=None, data=data)
            self.head = new_node
            self.tail = new_node
            return self.head
        for _ in range(mid - 1):
            curr = curr.next
        new_node = Node(prev=curr, next=curr.next, data=data)
        if curr.next:
            curr.next.prev = new_node
        curr.next = new_node
        if new_node.next is None:
            self.tail = new_node
        return self.head

    def insert_at_index(self, index, data):
        """
        insert at specific index of the DLL. Requires traversal to that index
        """
        list_length = len(self)
        if index > list_length:
            raise IndexError("index is larger than list")
        else:
            if index == 0:
                self.insert_head(data)
            elif index == list_length - 1 and list_length > 2:
                self.insert_tail(data)
            else:
                curr = self.head
                for i in range(list_length - 1):
                    if i == index - 1:
                        break
                    curr = curr.next
                new_node = Node(prev=curr, next=curr.next, data=data)
                if curr.next:
                    curr.next.prev = new_node
                curr.next = new_node
                if new_node.next is None:
                    self.tail = new_node
            return self.head

    def delete_at_head(self):
        """
        deletes the head node of the list. This is a constant time operation. The new head node becomes the node after the head
        if the old head was the tail as well, set the tail to None
        """
        if self.head == self.tail:
            self.head = self.tail = None
            return self.head
        next_node = self.head.next
        self.head = next_node
        if next_node is not None:
            next_node.prev = None
        return self.head

    def delete_at_tail(self):
        """
        requires traversing to the tail node. since we maintain a tail node, this may not be necessary.
        we just need to set the prev node to the tail node as the tail node
        if the tail node is the head node, then the list is empty
        """
        if self.tail == self.head:
            self.tail = self.head = None
            return self.head
        self.tail.prev.next = None
        self.tail = self.tail.prev
        return self.head

    def delete_at_index(self, index):
        """
        requires determining the length of the list, and then traversing to the index before the one we want to delete
        and then pointing the current node we are at to the next node after the one we want to delete
        """
        curr = self.head
        length = len(self)
        # edge case where list is empty
        if self.head is None:
            raise IndexError("list is empty")
        # edge case where length of the list is smaller than the index passed
        if index > length:
            raise IndexError("index larger than list size")
        # edge case where index points to the head
        if index == 0:
            next_node = self.head.next
            self.head = next_node
            if next_node is not None:
                next_node.prev = None
            return self.head
        for _ in range(index - 1):
            curr = curr.next
        node_to_delete = curr.next
        next_node = node_to_delete.next
        curr.next = node_to_delete.next
        if next_node is not None:
            next_node.prev = curr
        return self.head
