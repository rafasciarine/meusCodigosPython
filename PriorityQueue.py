class PriorityQueue:
    """
        Priority Queue class:

            - Must contain a function that checks whether the queue is empty
            - Must contain a function that inserts an item into the queue
            - Must contain a function that removes an item from the queue, with priority from highest to lowest
            - Must contain a function that spies the items in the queue
            - Must contain a function that returns the size of the queue
            - Must contain a function that empties the contents of the queue, according to the priority established
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
    def insert(self, item):
        self.items.append(item)

    ''' Function that removes an item from the queue, with priority from highest to lowest: '''
    def dequeue(self):
        maxi = 0

        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxi]:
                maxi = i

        item = self.items[maxi]
        self.items[maxi:maxi + 1] = []

        print(item)

    ''' Function that peeks the content of the queue: '''
    def peek(self):
        print(self.items)

    ''' Function that returns the size of the queue: '''
    def size(self):
        print(len(self.items))

    ''' Function that cleans the queue, according to the priority established '''
    def clean_queue(self):
        while len(self.items) != 0:
            self.dequeue()
