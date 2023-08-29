#!/usr/bin/python3
'''
100-singly_linked_list: implement singly_linked list using python class

Class SinglyLinkedList:
Class Node:
'''


class Node:
    '''
    Node(self, data, next_node=None)

    creat a node for the singly_linked list with the data as data and
    next_node as a reference to the next Node instance
    '''

    def __init__(self, data, next_node=None):
        '''
        Conistructer method
        '''
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        '''
        A property to retrive the self.__data attribute
        '''
        return self.__data

    @data.setter
    def data(self, value):
        '''
        A property to set the self.__data attribute
        '''
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def next_node(self):
        '''
        A property to retrive the self.__next_node attribute
        '''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''
        A property to setthe self.__next_node attribute
        '''
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    '''
    SinglyLinkedList()

    Creat a singly_linked_list and use the Node Class to creat nodes
    printable sorted Singly_linked_list class
    '''

    def __init__(self):
        '''
        Constructer method
        '''
        self.__head = None

    def __str__(self):
        '''
        Cosutmize the __str__ method
        '''
        __temp = self.__head
        while self.__head.next_node:
            print("{:d}".format(self.__head.data))
            self.__head = self.__head.next_node
        print("{:d}".format(self.__head.data), end="")
        self.__head = __temp
        return ""

    def sorted_insert(self, value):
        '''
        SinglyLinkedList.sorted_insert(self, value)

        Insert a node in a sorted order (increasing order)

        Args:
            value: the value of the new node
        '''
        __new_node = Node(value)
        __temp = self.__head
        __prev = None
        if self.__head is None:
            __new_node.next_node = None
            self.__head = __new_node
            return
        while self.__head:

            if self.__head.data > value:
                __new_node.next_node = self.__head

                if __prev:
                    __prev.next_node = __new_node
                    self.__head = __temp
                else:
                    self.__head = __new_node

                return

            __prev = self.__head
            self.__head = self.__head.next_node

        __new_node.next_node = None
        __prev.next_node = __new_node
        self.__head = __temp


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.sorted_insert(2)
    sll.sorted_insert(5)
    sll.sorted_insert(3)
    sll.sorted_insert(10)
    sll.sorted_insert(1)
    sll.sorted_insert(-4)
    sll.sorted_insert(-3)
    sll.sorted_insert(4)
    sll.sorted_insert(5)
    sll.sorted_insert(12)
    sll.sorted_insert(3)
    print(sll)
