import unittest

from datastructures.stacks import StackArrayImpl, StackLinkedListImpl


class TestStackArrayImpl(unittest.TestCase):

    def test_initialization(self):
        stack = StackArrayImpl()
        self.assertTrue(stack.isEmpty())

    def test_push(self):
        stack = StackArrayImpl()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.peek(), 2)

    def test_pop(self):
        stack = StackArrayImpl()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        with self.assertRaises(IndexError):
            stack.pop()

    def test_peek(self):
        stack = StackArrayImpl()
        stack.push(1)
        self.assertEqual(stack.peek(), 1)
        stack.push(2)
        self.assertEqual(stack.peek(), 2)
        stack.pop()
        self.assertEqual(stack.peek(), 1)
        stack.pop()
        with self.assertRaises(IndexError):
            stack.peek()

    def test_isEmpty(self):
        stack = StackArrayImpl()
        self.assertTrue(stack.isEmpty())
        stack.push(1)
        self.assertFalse(stack.isEmpty())
        stack.pop()
        self.assertTrue(stack.isEmpty())

    def test_search(self):
        stack = StackArrayImpl()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.search(2), 1)
        self.assertEqual(stack.search(4), -1)

    def test_size(self):
        stack = StackArrayImpl()
        self.assertEqual(stack.size(), 0)
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.size(), 2)
        stack.pop()
        self.assertEqual(stack.size(), 1)

class TestStackLinkedListImpl(unittest.TestCase):

    def test_initialization(self):
        stack = StackLinkedListImpl()
        self.assertTrue(stack.isEmpty())

    def test_push(self):
        stack = StackLinkedListImpl()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.peek(), 2)

    def test_pop(self):
        stack = StackLinkedListImpl()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        with self.assertRaises(IndexError):  # Assuming popping from empty stack raises AttributeError
            stack.pop()

    def test_peek(self):
        stack = StackLinkedListImpl()
        stack.push(1)
        self.assertEqual(stack.peek(), 1)
        stack.push(2)
        self.assertEqual(stack.peek(), 2)
        stack.pop()
        self.assertEqual(stack.peek(), 1)
        stack.pop()
        with self.assertRaises(IndexError):  # Assuming peeking from empty stack raises AttributeError
            stack.peek()

    def test_isEmpty(self):
        stack = StackLinkedListImpl()
        self.assertTrue(stack.isEmpty())
        stack.push(1)
        self.assertFalse(stack.isEmpty())
        stack.pop()
        self.assertTrue(stack.isEmpty())

    def test_search(self):
        stack = StackLinkedListImpl()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.search(2), 1)
        self.assertEqual(stack.search(4), -1)

    def test_size(self):
        stack = StackLinkedListImpl()
        self.assertEqual(stack.size(), 0)
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.size(), 2)
        stack.pop()
        self.assertEqual(stack.size(), 1)

if __name__ == '__main__':
    unittest.main()
