class Queue:
    def __init__(self):
        self.queue = DoublyLinkedList()

    def enqueue(self, data):
        # Přidá prvek na konec fronty
        self.queue.append(data)

    def dequeue(self):
        # Odebere prvek ze začátku fronty
        if self.queue.head:
            value = self.queue.head.data
            self.queue.delete(value)
            return value
        raise IndexError("dequeue from empty queue")

    def __iter__(self):
        return iter(self.queue)

    def __contains__(self, value):
        return value in self.queue

    def __str__(self):
        return str(self.queue)

    def __len__(self):
        return int(self.queue)

    def __add__(self, other):
        if not isinstance(other, Queue):
            raise TypeError("Can only add another Queue")
        combined_queue = Queue()
        combined_queue.queue = self.queue + other.queue
        return combined_queue

    def __iadd__(self, other):
        if not isinstance(other, Queue):
            raise TypeError("Can only add another Queue")
        self.queue += other.queue
        return self

    def __eq__(self, other):
        if not isinstance(other, Queue):
            return False
        return self.queue == other.queue

    def __del__(self):
        print("Deleting queue")
        del self.queue
