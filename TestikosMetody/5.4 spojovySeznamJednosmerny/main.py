class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next:
            current.next = current.next.next

    def __iter__(self):
        # Podporuje iteraci přes seznam
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __contains__(self, value):
        # Vrací True, pokud hodnota existuje v seznamu
        for node_data in self:
            if node_data == value:
                return True
        return False

    def __next__(self):
        # Podpora pro iterátor
        if self.current:
            data = self.current.data
            self.current = self.current.next
            return data
        else:
            raise StopIteration

    def __new__(cls):
        # Vytváří nový prázdný seznam
        return super(SinglyLinkedList, cls).__new__(cls)

    def __str__(self):
        # Vrací reprezentaci seznamu jako string
        return ' -> '.join(str(data) for data in self)

    def __int__(self):
        # Vrací počet uzlů jako celé číslo
        return sum(1 for _ in self)

    def __float__(self):
        # Vrací float reprezentaci součtu všech hodnot (pokud jsou numerické)
        return float(sum(node_data for node_data in self))

    def __add__(self, other):
        # Přidání dalšího spojového seznamu na konec
        if not isinstance(other, SinglyLinkedList):
            raise TypeError("Can only add another SinglyLinkedList")
        combined = SinglyLinkedList()
        for data in self:
            combined.append(data)
        for data in other:
            combined.append(data)
        return combined

    def __sub__(self, other):
        # Odebere prvky obsažené v jiném seznamu
        if not isinstance(other, SinglyLinkedList):
            raise TypeError("Can only subtract another SinglyLinkedList")
        result = SinglyLinkedList()
        for data in self:
            if data not in other:
                result.append(data)
        return result

    def __iadd__(self, other):
        # Přidání in-place, tedy připojení prvků dalšího seznamu
        if not isinstance(other, SinglyLinkedList):
            raise TypeError("Can only add another SinglyLinkedList")
        for data in other:
            self.append(data)
        return self

    def __isub__(self, other):
        # Odebrání in-place
        if not isinstance(other, SinglyLinkedList):
            raise TypeError("Can only subtract another SinglyLinkedList")
        for data in other:
            self.delete(data)
        return self

    def __eq__(self, other):
        # Porovnání dvou seznamů
        if not isinstance(other, SinglyLinkedList):
            return False
        return list(self) == list(other)

    def __lt__(self, other):
        # Porovnání počtu prvků v seznamu
        if not isinstance(other, SinglyLinkedList):
            raise TypeError("Can only compare with another SinglyLinkedList")
        return len(list(self)) < len(list(other))

    def __hash__(self):
        # Hashuje seznam
        return hash(tuple(self))

    def __del__(self):
        # Destruktor, který uvolní paměť
        print("Deleting linked list")
        self.head = None
