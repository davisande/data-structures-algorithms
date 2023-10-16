class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        main_node = Node(value)
        self.__head = main_node
        self.__tail = main_node
        self.__length = 1

    def append(self, value):
        new_node = Node(value)
        if self.__length == 0:
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.next = new_node
            self.__tail = self.__tail.next

        self.__length += 1

    def pop(self):
        if self.__length == 0:
            return None

        current = self.__head
        before = self.__head
        while current.next:
            before = current
            current = current.next

        self.__tail = before
        self.__tail.next = None
        self.__length -= 1

        if self.__length == 0:
            self.__head = None
            self.__tail = None

        return current.value

    def prepend(self, value):
        new_node = Node(value)
        if self.__length == 0:
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.next = self.__head
            self.__head = new_node

        self.__length += 1

    def pop_first(self):
        if self.__length == 0:
            return

        current = self.__head
        self.__head = self.__head.next
        current.next = None
        self.__length -= 1

        if self.__length == 0:
            self.__tail = None

        return current.value

    def get(self, index):
        node = self.__get_node(index)
        if node is None:
            return None

        return node.value

    def set(self, index, value):
        current = self.__get_node(index)
        if current:
            current.value = value
            return True

        return False

    def insert(self, index, value):
        if index < 0 or index >= self.__length:
            return

        if index == 0:
            self.prepend(value)
        elif index == self.__length - 1:
            self.append(value)
        else:
            new_node = Node(value)
            before = self.__get_node(index - 1)
            new_node.next = before.next
            before.next = new_node
            self.__length += 1

    def remove(self, index):
        if index < 0 or index >= self.__length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.__length - 1:
            return self.pop()

        before = self.__get_node(index - 1)
        current = before.next
        before.next = current.next
        self.__length -= 1

        return current.value

    def reverse(self):
        current = self.__head
        self.__head = self.__tail
        self.__tail = current
        before = None

        for _ in range(self.__length):
            after = current.next
            current.next = before
            before = current
            current = after

    def __get_node(self, index):
        if index < 0 or index >= self.__length:
            return None

        current = self.__head
        for _ in range(index):
            current = current.next

        return current

    def __str__(self):
        values = ''
        current = self.__head
        while current:
            values += str(current.value)
            current = current.next

        return values
