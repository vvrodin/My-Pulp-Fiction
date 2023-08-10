class Node:
    def __init__(self, *args, first_init=False):
        if first_init:
            self.data = None
        else:
            self.data = list(*args)
        self.next_node = None
        return

    def __str__(self):
        return str(self.data)


class Linked_list:
    def __init__(self):
        self.head = Node(None, first_init=True)
        self.head.next_node = Node(None, first_init=True)

    def add(self, *args):
        args = list(args)
        if self.head.data is None:
            self.head.data = args
            return None
        elif self.head.next_node.data is None:
            self.head.next_node.data = args
            return None
        node = self.head
        while node.next_node is not None:
            node = node.next_node
        node.next_node = Node(args)

    def find(self, *element):
        element = list(element)
        node = self.head
        while node.data != element and node.next_node is not None:
            node = node.next_node
        if node.data == element:
            return node
        if node.data != element:
            return -1

    def remove(self, *element):
        element = list(element)
        node = self.head
        previous_node = -1
        while node.data != element and node.next_node is not None:
            previous_node = node
            node = node.next_node
        if node.data == element and node.next_node is None:
            previous_node.next_node = None
        if node.next_node is None and node.data != element:
            raise KeyError
        if previous_node == -1:
            self.head = self.head.next_node
            return
        previous_node.next_node = node.next_node
        return

    def show_list(self):
        node = self.head
        while node.next_node is not None:
            print(node, end=' - ')
            node = node.next_node
        print(node)