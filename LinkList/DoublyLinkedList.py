# Doubly Link List


class Node(object):
    """
    Create Node at every call ['prev'|'data' | 'next']
    """
    def __init__(self, data=None, next=None, prev=None):
        self.prev = prev
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


class DoublyLinkList(object):
    """
    Operations with Link list.
    """
    def __init__(self):
        self.head = None

    def __repr__(self):
        ll_list = []
        current = self.head
        while current:
            ll_list.append(repr(current))
            current = current.next
        return '['+', '.join(ll_list)+']'

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def insert(self, data, index):
        """
        Data to be insert at index location.
        :param data: Data to be insert.
        :param index: location where data added.
        :return: None
        """

    def append(self, data):
        """
        Data to be insert at end of list.
        :param data: Data to be insert.
        :return: None
        """
        if not self.head:
            self.head = Node(data=data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data=data, prev=current)

    def prepend(self, data):
        """
        Data to be insert at beginning of list.
        :param data: Data to be insert.
        :return: None
        """
        new_node = Node(data=data)
        current = self.head
        if current:
            new_node.next = current
            current.prev = new_node
        self.head = new_node

    def remove(self, key):
        """
        Remove the data from list
        :param key: data which will be removed
        :return: None
        """
        current = self.head
        while current and current.data != key:
            current = current.next
        if not current:
            return
        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
        if current is self.head:
            self.head = current.next
        current.next = None
        current.prev = None

    def search(self, key):
        """
        Search data in list.
        :param key: data to be searched.
        :return: obj
        """
        current = self.head
        while current and current.data != key:
            current = current.next
        return current

    def reverse(self):
        """
        Reverse the list.
        :return: None
        """
        current = self.head
        prev_node = None
        while current:
            prev_node = current.prev
            current.prev = current.next
            current.next = prev_node
            current = current.prev
        self.head = prev_node.prev

    def is_palindrome(self):
        """
        Check whether list is palindrome.
        :return: bool
        """
        current = self.head
        data_list = []
        while current:
            data_list.append(current.data)
            current = current.next
        return data_list == data_list[::-1]

