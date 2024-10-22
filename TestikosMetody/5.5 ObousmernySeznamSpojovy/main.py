class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = DoublyNode(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, data):
        new_node = DoublyNode(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def delete(self, data):
        if not self.head:
            return
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                return
            current = current.next

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __contains__(self, value):
        for node_data in self:
            if node_data == value:
                return True
        return False

    def __next__(self):
        if self.current:
            data = self.current.data
            self.current = self.current.next
            return data
        else:
            raise StopIteration

    def __new__(cls):
        return super(DoublyLinkedList, cls).__new__(cls)

    def __str__(self):
        return ' <-> '.join(str(data) for data in self)

    def __int__(self):
        return sum(1 for _ in self)

    def __float__(self):
        return float(sum(node_data for node_data in self))

    def __add__(self, other):
        if not isinstance(other, DoublyLinkedList):
            raise TypeError("Can only add another DoublyLinkedList")
        combined = DoublyLinkedList()
        for data in self:
            combined.append(data)
        for data in other:
            combined.append(data)
        return combined

    def __sub__(self, other):
        if not isinstance(other, DoublyLinkedList):
            raise TypeError("Can only subtract another DoublyLinkedList")
        result = DoublyLinkedList()
        for data in self:
            if data not in other:
                result.append(data)
        return result

    def __iadd__(self, other):
        if not isinstance(other, DoublyLinkedList):
            raise TypeError("Can only add another DoublyLinkedList")
        for data in other:
            self.append(data)
        return self

    def __isub__(self, other):
        if not isinstance(other, DoublyLinkedList):
            raise TypeError("Can only subtract another DoublyLinkedList")
        for data in other:
            self.delete(data)
        return self

    def __eq__(self, other):
        if not isinstance(other, DoublyLinkedList):
            return False
        return list(self) == list(other)

    def __lt__(self, other):
        if not isinstance(other, DoublyLinkedList):
            raise TypeError("Can only compare with another DoublyLinkedList")
        return len(list(self)) < len(list(other))

    def __hash__(self):
        return hash(tuple(self))

    def __del__(self):
        print("Deleting doubly linked list")
        self.head = None
        self.tail = None
