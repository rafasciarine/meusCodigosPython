class Deque:
    """
        Deque class:
            - Must have a function that checks if the deck is empty
            - Must have a function that adds at the end
            - Must have a function that adds at the beginning
            - Must have a function that removes at the end
            - Must have a function that removes at the beginning
            - Must have a function that returns the size of the deque
            - Must have a function that visualizes the deque items
        """

    ''' Function that starts the deque: '''
    def __init__(self):
        self.items = []

    ''' Function that checks the deque os empty: '''
    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    ''' Function that enqueues an item at the end of the deque: '''
    def enqueue_front(self, item):
        self.items.append(item)

    ''' Function that enqueues an item at the beginning the deque: '''
    def enqueue_rear(self, item):
        self.items.insert(0, item)

    ''' Function that dequeues an item at the end of the deque: '''
    def dequeue_front(self):
        if not self.is_empty():
            return self.items.pop(-1)

    ''' Function that dequeues an item at the beginning of the deque: '''
    def dequeue_rear(self):
        if not self.is_empty():
            return self.items.pop(0)

    ''' Function that checks the deque content: '''
    def peek(self):
        print(self.items)

    ''' Function that returns the deque size: '''
    def size(self):
        print(len(self.items))

    ''' Function that cleans the queue: '''
    def clean_queue(self, side):
        if side == 1:       # option 1 dequeues at the rear
            self.dequeue_rear()
        if side == 2:       # option 2 dequeues at the front
            self.dequeue_front()
