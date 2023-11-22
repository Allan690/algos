"""
A linked list is a fundamental data structure used in computer science to organize elements in a sequential manner

Structure: a linked list is a sequence of nodes where each node contains data and a reference to the next node in the sequence
First node is called the head and the last node links to a null reference, indicating the end of the list.

Linked lists are dynamic. They can grow or shrink as needed at runtime, which makes them more flexible for certain types
of operations.

Each node is stored independently in memory(unlike in arrays where elements are stored in contiguous memory locations)

Uses and applications:

Due to these 3 characteristics:
1. Dynamic memory allocations
2. Efficient insertion
3. Efficient deletion

Lists can be used for various applications:

1. Dynamic memory allocation -> where the size of the data structure can change during run time.
2. Implementation of other data structures -> e.g stacks, queues, hash tables, adjacency lists etc.
3. Undo functionality in applications -> each node represents a state of the document or file.
4. Memory management in operating systems -> used in managing free blocks of memory in operating systems
5. Implementation of hash tables -> collision in hash tables can be used to handle multiple items that hash to the same index.
6. Handling large data records -> when dealing with large records where inserting or deleting items in the middle is common,
linked list can be more efficient than arrays.
7. Circular lists for round-robin scheduling -> in certain algorithms, like round-robin scheduling, circular linked lists can be used
for their ability to cycle through nodes repeatedly.
8. Sparse matrices -> in sparse matrices most elements are zero, linked list nodes are used to hold non-zero elements.


Access times:

1. Accessing an element(search)
- Average case: O(n)
- Worst case: O(n)

Explanations: To access an element, you generally need to start at the head and follow
the links until you find the desired element

2. Inserting
- at the head O(1)
- At the tail -> O(n) for a singly linked list and O(1) for a doubly linked list
explanation: inserting at the head is fast, but elswhere requires list traversal.

3. Deleting
- at the head O(1)
- At tail-> O(n) for a singly linked list and O(1) for a doubly linked list
- In the middle -. O(n)

4. Finding length
Avg case: O(n)
worst: O(n)
Explanation: You must traverse the entire list to count all elements.

5. Traversal
avg case: O(n)
worst: O(n)
Explanation: Traversing the entire list requires looking at each element once.

"""

class Node:
    """
    represents a node in a linked list. A node has data and a reference to the next node
    """
    def __init__(self, data, next) -> None:
        self.data = data
        self.next = next


class LinkedList:
    """
    this is the linked list of nodes. A linked list has a head node and optional tail node
    """
    def __init__(self, head: Node = None, tail: Node = None) -> None:
        self.head = head
        self.tail = tail

    def search(self, data):
        """
        to search for a node in the list requires traversal through all the nodes in the list
        O(N)
        """
        temp = self.head
        while temp:
            if temp.data == data:
                return temp
            temp = temp.next
        raise ValueError('Node with the data passed in was not found')


    def insert_head(self, data):
        """
        inserts a node at the head of the linked list.
        This is a O(1) - constant time operation
        """
        if self.head is not None:
            new_node = Node(data=data, next=self.head)
            self.head = new_node
        else:
            new_node = Node(data=data, next=None)
            self.head = new_node

    def insert_tail(self, data):
        """
        inserts a node at the tail of the linked list.
        This requires traversal through the list to find the tail node(if a tail node is not maintained).
        This is O(n) time operation
        """
        temp = self.head
        if temp is None:
            new_node = Node(data=data, next=None)
            self.head = new_node
        while temp.next:
            temp = temp.next
        new_node = Node(data=data, next=None)
        temp.next = new_node
        self.tail = temp.next

    def length(self):
        """
        determines the length of a linked list.
        This requires traversal through the length of the list, keeping track of the count of nodes
        """
        temp = self.head
        count = 0
        while temp is not None:
            count +=1
            temp = temp.next
        return count


    def insert_middle(self, data):
        """
        inserts a new node in the middle of the linked list.
        this requires, first, determining the length of the list
        and second, traversal of the list to the mid-lenght of the list to perform the insertion after the element at mid
        """
        if self.head is None:
            # if the list is empty insert at the head
            self.insert_head(data)
            return
        list_length = self.length()
        mid = list_length // 2

        curr = self.head
        for _ in range(mid - 1):
            curr = curr.next

        # create a new node and insert it after the current node
        new_node = Node(data=data, next=curr.next)
        curr.next = new_node


    def insert_at_index(self, index, data):
        """
        inserts a new node at a specific index of the linked list.
        this requires, first, traversal to the specified index. If the index is larger than the list, throw index error,
        else insert at that index
        """
        if self.head is None and index != 0:
            raise ValueError('list is empty')
        if index == 0:
            new_node = Node(data=data, next=self.head.next)
            self.head = new_node
        else:
            try:
                curr = self.head
                for _ in range(index - 1):
                    curr = curr.next
                new_node = Node(data=data, next=curr.next)
                curr.next = new_node
            except:
                raise IndexError('specified index is larger than allowed')

    def print_list(self):
        """
        prints the linked list to stdout
        """
        curr = self.head
        output = ""
        while curr:
            output += str(curr.data) + "->"
            curr = curr.next
        return output

    def delete_at_index(self, index):
        """
        deletes a new node at a specific index of the linked list.
        this requires, first, traversal to the index before specified index. If the index is larger than the list, throw index error,
        else delete at that index
        """
        if self.head is None and index != 0:
            raise ValueError('list is empty')
        if index == 0:
            self.delete_at_head()
            return
        else:
            try:
                curr = self.head
                for _ in range(index - 1):
                    curr = curr.next
                curr.next = curr.next.next
            except:
                raise IndexError('specified index is larger than allowed')

    def delete_at_head(self):
        """
        removes an element at the head of the linked list. This is an O(1) operation
        """
        if self.head is None:
            raise ValueError('linked list is empty')
        self.head = self.head.next
        return self.head

    def delete_at_tail(self):
        """
        removes an element at the tail of the linked list.
        This first requires traversal through the linked list to the element before the tail,
        then pointing it to a null reference thus deleting the tail
        """
        temp = self.head
        length = self.length()
        for _ in range(length - 2):
            temp = temp.next
        temp.next = None
        self.tail = temp
