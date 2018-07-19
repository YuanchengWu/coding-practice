class LinkedList:
    head = None

    def __init__(self, data):
        self.head = Node(data[0])
        temp = self.head
        for value in data[1:]:
            temp.next = Node(value)
            temp = temp.next

    def __str__(self):
        temp = self.head
        out = []
        while temp:
            out.append(temp.value)
            temp = temp.next
        return str(out)

    def insert(self, value, index):
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        new_node = Node(value)
        new_node.next = temp.next
        temp.next = new_node

    def delete(self, index):
        if index == 0:
            self.head = self.head.next
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            temp.next = temp.next.next


class Node:
    next = None

    def __init__(self, value):
        self.value = value

llist = LinkedList([1, 2, 3, 4])
print(llist)
llist.insert(5, 4)
print('after insert:', llist)
llist.delete(4)
print('after delete:', llist)