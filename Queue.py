class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def size(self):
        print(len(self.items))

    def peek(self):
        print(self.items)


q = Queue()
q.enqueue('olá')
q.enqueue('oi')
q.dequeue()

q.peek()
