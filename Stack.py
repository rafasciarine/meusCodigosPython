class Stack:
    """
        Stack class:
            - Must have a function that does the stacking
            - Must have a function that does the unstacking
            - Must have a function that returns the stack size
            - Must have a function that makes the stack unstacked instantly
    """

    ''' Function that starts the stack: '''

    def __init__(self):
        self.items = []

    ''' Function that checks if the stack is empty: '''

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    ''' Function that adds an item to the stack: '''

    def push(self, item):
        self.items.append(item)

    ''' Function that removes an item from the stack: '''

    def pop(self):
        if not self.is_empty():
            return self.items.pop(-1)

    ''' Function that peeks at the contents of the stack: '''

    def peek(self):
        print(self.items)

    ''' Function that returns the stack size: '''

    def size(self):
        print(len(self.items))

    ''' Function that clears the contents of the stack: '''

    def clean_stack(self):
        while len(self.items) != 0:
            self.pop()

    ''' Function that returns the top of the stack: '''

    def top(self):
        print(self.items[-1])
