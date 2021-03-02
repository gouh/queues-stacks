from .node import Node

class Queue:
    def __init__(self): 
        self.front = None 
        self.rear = None

    # This method make easy interpolation
    def __str__(self):
        cur = self.front
        out = ""
        while cur:
            out += str(cur.value) + " "
            cur = cur.next
        return out[:-1]

    # Enqueue value
    def add(self, value): 
        new_node = Node(value) 
        if self.rear == None:
            self.front = new_node 
            self.rear = new_node 
            return
        self.rear.next = new_node 
        self.rear = new_node 

    # Returns and removes the front of the queue. Throws an exception if the queue is empty.
    def remove(self): 
        if self.is_empty(): 
            raise Exception("Queue is empty")
        first = self.front 
        self.front = first.next
        if(self.front == None): 
            self.rear = None
        return first.value

    # Returns the front of the queue. Returns null if the queue is empty.
    def peek(self):
        if self.is_empty():
            return None
        return self.front.value

    # Check if the queue is empty
    def is_empty(self): 
        return self.front == None
