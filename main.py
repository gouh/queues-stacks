from structure import Queue
from structure import Stack

# Inverse queue
if __name__ == '__main__':
    input_queue = Queue()
    input_queue.add("example")
    input_queue.add("with")
    input_queue.add("Queue")

    stack = Stack(maxsize = 3)
    while not stack.is_full():
        stack.push(input_queue.remove())

    output_queue = Queue()
    while not stack.is_empty():
        output_queue.add(stack.pop())

    print(f"{output_queue}")