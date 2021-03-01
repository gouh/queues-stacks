class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, maxsize):
        # Este nodo solo se utiliza como utileria no se muestra
        self.head_node = Node("Nodo principal")
        self.size = 0
        self.maxsize = maxsize

    def __str__(self):
        cur = self.head_node.next
        out = ""
        while cur:
            out += str(cur.value) + "=>"
            cur = cur.next
        return out[:-2]

    def pop(self):
        if self.is_empty():
            raise Exception("La pila esta vacía")
        remove = self.head_node.next
        self.head_node.next = self.head_node.next.next
        self.size -= 1
        return remove.value

    def push(self, value):
        if self.size == self.maxsize:
            raise Exception("La pila esta llena")
        node = Node(value)

        # Apunta al nodo que el nodo principal tenga como siguiente
        node.next = self.head_node.next

        # El nodo principal apunta ahora al nuevo nodo
        self.head_node.next = node
        self.size += 1

    def peek(self):
        if self.is_empty():
            raise Exception("La pila esta vacía")
        return self.head_node.next.value

    def is_empty(self):
        return self.size == 0

    def is_full(self):
      return self.size == self.maxsize


stack = Stack(maxsize = 3)
stack.push("Hola mundo")
print(f"La pila solo tiene un valor: {stack}")
stack.pop()
print(f"La pila debe estar vacía: {bool(stack.is_empty())}")
stack.push(1)
stack.push(2)
stack.push(3)
print(f"El ultimo valor de la pila es 3: {stack.peek()}")
print(f"La pila esta llena: {stack.is_full()}")