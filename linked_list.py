class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next_node = None

    def __repr__(self) -> str:
        return f"<Node data:{self.data}>"


class LinkedList:

    """
    Singly linked list
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        returns no of nodes in the list
        Takes 0(n) time
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node
        return count

    def add(self, data):
        """
        adds new node containing data at the head of the lst
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        searches for the first node containing data that matches the key
        Takes 0(n) - linear time
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            current = current.next_node
        return None

    def insert(self, data, index):
        if index == 0:
            self.add(data)
            return

        new_node = Node(data)
        before_position = index - 1
        current = self.head

        while before_position != 0:
            current = current.next_node
            before_position -= 1

        next_node = current.next_node
        current.next_node = new_node
        new_node.next_node = next_node

    def remove(self, index):
        if index == 0:
            self.head = self.head.next_node
            return
        before_position = index - 1
        current = self.head

        while before_position != 0:
            current = current.next_node
            before_position -= 1
        pre_position = current
        position = current.next_node
        post_position = position.next_node

        pre_position.next_node = post_position

    def __repr__(self) -> str:
        """
        returns a string representation of the list.
        Takes 0(n) time
        """

        nodes = []
        current = self.head
        print(current)
        while current:
            nodes.append(f"{current.data}")
            current = current.next_node
        return "->".join(nodes)


linkedList = LinkedList()
linkedList.add(20)
linkedList.add(30)
linkedList.add(230)
linkedList.add(30)
linkedList.add(10)
linkedList.add(50)

print(linkedList.head)
print(linkedList)
