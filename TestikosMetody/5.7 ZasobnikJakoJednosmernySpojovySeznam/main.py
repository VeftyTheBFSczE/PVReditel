class Stack:
    def __init__(self):
        self.stack = SinglyLinkedList()

    def push(self, data):
        # Přidá prvek na vrchol zásobníku
        self.stack.prepend(data)

    def pop(self):
        # Odebere prvek z vrcholu zásobníku
        if self.stack.head:
            value = self.stack.head.data
            self.stack.delete(value)
            return value
        raise IndexError("pop from empty stack")

    def peek(self):
        # Vrátí prvek z vrcholu zásobníku bez odebrání
        if self.stack.head:
            return self.stack.head.data
        raise IndexError("peek from empty stack")

    def __iter__(self):
        return iter(self.stack)

    def __contains__(self, value):
        return value in self.stack

    def __str__(self):
        return str(self.stack)

    def __len__(self):
        return int(self.stack)

    def __add__(self, other):
        if not isinstance(other, Stack):
            raise TypeError("Can only add another Stack")
        combined_stack = Stack()
        combined_stack.stack = self.stack + other.stack
        return combined_stack

    def __iadd__(self, other):
        if not isinstance(other, Stack):
            raise TypeError("Can only add another Stack")
        self.stack += other.stack
        return self

    def __eq__(self, other):
        if not isinstance(other, Stack):
            return False
        return self.stack == other.stack

    def __del__(self):
        print("Deleting stack")
        del self.stack
