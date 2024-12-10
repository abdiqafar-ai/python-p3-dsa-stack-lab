class Stack:
    def __init__(self, items=None, limit=100):
        if items is None:
            items = []
        self.items = items  # List to hold the stack elements
        self.limit = limit  # Maximum limit for the stack

    def isEmpty(self):
        """Check if the stack is empty"""
        return len(self.items) == 0

    def push(self, item):
        """Push an item to the stack"""
        if len(self.items) < self.limit:  # Check if stack is full before adding
            self.items.append(item)
        else:
            raise Exception("Stack is full")  # Raise an error if stack exceeds the limit

    def pop(self):
        """Pop an item from the stack"""
        if self.isEmpty():
            return None  # Return None if the stack is empty
        return self.items.pop()

    def peek(self):
        """Return the top item without removing it from the stack"""
        if self.isEmpty():
            raise Exception("Stack is empty")  # Raise an error if stack is empty
        return self.items[-1]

    def size(self):
        """Return the number of items in the stack"""
        return len(self.items)

    def full(self):
        """Check if the stack is full"""
        return len(self.items) == self.limit  # Stack is full when its size matches the limit

    def search(self, target):
        """Search for an item in the stack and return its position from the bottom (1-based index)"""
        try:
            # Find the index from the bottom of the stack (not the top)
            index_from_bottom = len(self.items) - self.items.index(target) - 1
            return index_from_bottom
        except ValueError:
            return -1  # Return -1 if the item is not found
