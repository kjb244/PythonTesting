from typing import TypeVar, Union, List

T = TypeVar('T')


class Node:
    def __init__(self, item: T):
        self.item = item
        self.next = None


class LinkedList:
    head: Union[None, Node] = None
    tail: Union[None, Node] = None

    def add_head(self, item: T) -> None:
        n = Node(item)
        if self.head is None:
            self.head = n
            self.tail = self.head
        else:
            self.tail = self.head
            n.next = self.head
            self.head = n

    def add_last(self, item: T) -> None:
        n = Node(item)
        if self.head is None:
            self.head = n
            self.tail = self.head
        else:
            self.tail.next = n
            self.tail = self.tail.next

    def find_all_indexes(self, item: T) -> list[int]:
        rtn_arr = []
        cntr = 0
        temp = self.head

        while temp is not None:
            if item == temp.item:
                rtn_arr.append(cntr)
            cntr += 1
            temp = temp.next
        return rtn_arr

    def find_first_and_remove(self, item: T) -> None:
        if self.head.item == item:
            self.head = self.head.next
        else:
            temp = self.head
            while temp.next is not None:
                if temp.next.item == item:
                    temp.next = temp.next.next
                    #last item then set tail
                    if temp.next is None:
                        self.tail = temp
                    break
                temp = temp.next



    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.item)
            temp = temp.next


l = LinkedList()
l.add_head('h')
l.add_head('k')
l.add_last('r')
l.add_last('p')
l.add_last('w')
l.find_first_and_remove('w')
l.add_last('z')
l.find_first_and_remove('z')
l.add_last('k')
l.find_first_and_remove('a')

l.print()
