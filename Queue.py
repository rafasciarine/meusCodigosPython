class Queue:
    """
        Queue class:

            - Must contain a function that checks whether the queue is empty
            - Must contain a function that inserts an item into the queue
            - Must contain a function that removes an item from the queue
            - Must contain a function that spies the items in the queue
            - Must contain a function that returns the size of the queue
            - Must contain a function that empties the contents of the queue
    """

    ''' Function that starts the queue: '''
    def __init__(self):
        self.items = []

    ''' Function that checks if the queue is empty: '''
    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    ''' Function that adds an item to the queue: '''
    def enqueue(self, item):
        self.items.append(item)

    ''' Function that removes an item from the queue: '''
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    ''' Function that returns the size of the queue: '''
    def size(self):
        print(len(self.items))

    ''' Function that peeks the content of the queue: '''
    def peek(self):
        print(self.items)
