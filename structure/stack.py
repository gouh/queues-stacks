from .node import Node

class Stack:
    def __init__(self, maxsize):
        self.head_node = Node("head node")
        self.size = 0
        self.maxsize = maxsize

    # This method make easy interpolation
    def __str__(self):
        cur = self.head_node.next
        out = ""
        while cur:
            out += str(cur.value) + " "
            cur = cur.next
        return out[:-1]
    
    # Add element to stack
    def push(self, value):
        if self.size == self.maxsize:
            raise Exception("Stack is full")
        node = Node(value)
        node.next = self.head_node.next
        self.head_node.next = node
        self.size += 1

    # Remove head from stack and get value
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        remove = self.head_node.next
        self.head_node.next = self.head_node.next.next
        self.size -= 1
        return remove.value

    # Get head value
    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.head_node.next.value

    # Check if stack is empty
    def is_empty(self):
        return self.size == 0

    # Check if stack is full
    def is_full(self):
      return self.size == self.maxsize
