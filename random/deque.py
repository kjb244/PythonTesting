from typing import TypeVar, Union, Generic

T = TypeVar('T')


class Deque():
    max_size = 3
    arr = [None for x in range(0, max_size)]
    front = -1
    tail = -1
    currSize = 0

    def print(self) -> None:
        print(self.arr)

    def add_first(self, item: T) -> None:
        self.maybe_resize()
        self.currSize = self.currSize + 1
        if self.front == -1:
            self.front = 0
            self.tail = 0
        else:
            if self.front - 1 < 0:
                self.front = self.max_size - 1
            else:
                self.front = self.front - 1
        self.arr[self.front] = item

    def add_last(self, item: T) -> None:
        self.maybe_resize()
        self.currSize = self.currSize + 1
        if self.front == -1:
            self.front = 0
            self.tail = 0
        else:
            if self.tail + 1 > self.max_size - 1:
                self.tail = 0
            else:
                self.tail = self.tail + 1
        self.arr[self.tail] = item

    def remove_first(self) -> Union[T, None]:
        if self.front != -1:
            self.currSize = self.currSize - 1
            rtn_value = self.arr[self.front]
            self.arr[self.front] = None

            if self.front + 1 > self.max_size - 1:
                self.front = 0
            else:
                self.front = self.front + 1

            if self.currSize == 0:
                self.front = - 1
                self.tail = -1
            return rtn_value
        return None

    def remove_last(self) -> Union[T, None]:
        if self.front != -1:
            self.currSize = self.currSize - 1
            rtn_value = self.arr[self.tail]
            self.arr[self.tail] = None

            if self.tail - 1 < 0:
                self.tail = self.max_size - 1
            else:
                self.tail = self.tail - 1

            if self.currSize == 0:
                self.front = - 1
                self.tail = -1

            return rtn_value
        return None

    def maybe_resize(self) -> None:

        if self.currSize + 1 > self.max_size:
            temp_arr = [None for x in range(0, self.max_size * 2)]
            front_pos = self.front
            counter = 0

            while self.arr[front_pos] is not None and counter < self.max_size:
                temp_arr[counter] = self.arr[front_pos]
                if front_pos + 1 > self.max_size - 1:
                    front_pos = 0
                else:
                    front_pos += 1
                counter += 1

            self.arr = temp_arr
            self.front = 0
            self.tail = counter - 1
            self.max_size *= 2


d = Deque()
d.add_first('f1')
d.add_first('f2')
d.add_last('l1')
d.add_last('l2')
d.add_first('f3')
d.print()
d.remove_last()
d.remove_last()
d.remove_last()
d.add_last('l1')
d.add_last('l2')
d.add_first('f4')
d.add_last('l4')
d.remove_last()
d.remove_last()
d.remove_last()
d.remove_last()
d.remove_last()
d.add_last('l5')
d.remove_last()
d.remove_last()
d.add_last('k')
d.add_first('b')
d.print()
print(d.remove_first())
print(d.remove_first())
print(d.remove_first())
print(d.remove_first())
d.add_last('k')
d.print()
