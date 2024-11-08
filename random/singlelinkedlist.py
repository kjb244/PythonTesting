from typing import TypeVar, Union

T = TypeVar('T')


class Node:
    def __init__(self, item: T):
        self.item = item
        self.next = None


class LinkedList:
    head: Union[None, Node] = None
    tail_pointer: Union[None, Node] = None

    def add_head(self, item: T) -> None:
        n = Node(item)
        if self.head is None:
            self.head = n
        else:
            n.next = self.head
            self.head = n

    def add_last(self, item: T) -> None:
        n = Node(item)
        if self.head is None:
            self.head = n
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = n

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.item)
            temp = temp.next


l = LinkedList()
l.add_head('h')
l.add_head('k')
l.add_last('r')
l.print()
