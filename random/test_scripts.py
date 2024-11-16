import unittest2

from singlelinkedlist import LinkedList


class TestLinkedList(unittest2.TestCase):

    def test_blank_head(self):
        ll = LinkedList()
        self.assertEqual(ll.to_list(), [])
    def test_one_element_head(self):
        ll = LinkedList()
        ll.add_head('a')
        self.assertEqual(ll.to_list(), ['a'])

    def simple_removals_by_index(self):
        ll = LinkedList
        ll.add_head('a')
        ll.add_last('b')
        ll.add_last('c')
        ll.remove_by_index(0)
        ll.add_last(1)
        ll.add_last('d')
        self.assertEqual(ll.to_list(), ['b', 'd'])



if __name__ == '__main__':
    unittest2.main()