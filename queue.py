class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self): 
        self.front = None 
        self.rear = None

    def __str__(self):
        cur = self.front
        out = ""
        while cur:
            out += str(cur.value) + "=>"
            cur = cur.next
        return out[:-2]

    def add(self, value): 
        new_node = Node(value) 
        if self.rear == None:
            self.front = new_node 
            self.rear = new_node 
            return
        self.rear.next = new_node 
        self.rear = new_node 

    def get(self): 
        if self.is_empty(): 
            raise Exception("La cola esta vacía")
        
        # Obtiene el primer valor de la cola
        first = self.front 

        # Reasigna el primer valor
        self.front = first.next

        # En caso de que el primer valor no exista entonces
        # La cola queda vacía
        if(self.front == None): 
            self.rear = None

    def is_empty(self): 
        return self.front == None

queue = Queue()
print(f"La cola debe estar vacía: {queue.is_empty()}")
queue.add(1)
queue.add(2)
queue.add(3)
print(f"Ahora esta es la representación de la fila: {queue}")
queue.get()
print(f"Ahora la pila solo debe tener 2 y 3: {queue}")