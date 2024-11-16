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

    def remove_by_index(self, index: int) -> Union[T, None]:
        if index > -1 and self.head is not None:

            temp_item = None
            if index == 0:
                temp_item = self.head.item
                self.head = self.head.next
                if self.head is None or self.head.next is None:
                    self.tail = self.head

            else:
                cntr = 1
                temp = self.head
                while temp.next is not None:
                    if cntr == index:
                        temp_item = temp.next.item
                        temp.next = temp.next.next
                        if temp.next is None:
                            self.tail = temp
                        break
                    temp = temp.next
                    cntr += 1
            return temp_item

    def find_first_and_remove(self, item: T) -> None:
        if self.head.item == item:
            self.head = self.head.next
            if self.head is None or self.head.next is None:
                self.tail = self.head
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

    def to_list(self) -> List[T]:
        temp = self.head
        arr = []
        while temp is not None:
            arr.append(temp.item)
            temp = temp.next
        return arr

    def print(self) -> None:
        temp = self.head
        str = ''
        while temp is not None:
            str += temp.item + ' '
            temp = temp.next
        print(str)


l = LinkedList()
l.add_head('a')
l.remove_by_index(0)
l.add_head('a')
l.add_last('b')
l.remove_by_index(0)
l.find_first_and_remove('b')
l.add_last('a')
l.add_last('b')
l.add_head('c')
l.remove_by_index(2)
l.add_head('b')
l.print()
