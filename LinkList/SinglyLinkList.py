# Singly Link List


class Node(object):
    """
    Create Node at every call ['data' | 'next']
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


class SinglyLinkList(object):
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
        if index == 0:
            self.prepend(data=data)
        elif len(self)-1 == index:
            self.append(data=data)
        else:
            current = self.head
            for i in range(index-1):
                current = current.next
            current.next = Node(data=data, next=current.next)

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

        current.next = Node(data=data)

    def prepend(self, data):
        """
        Data to be insert at beginning of list.
        :param data: Data to be insert.
        :return: None
        """
        self.head = Node(data, self.head)

    def remove(self, key):
        """
        Remove the data from list
        :param key: data which will be removed
        :return: None
        """
        current = self.head
        previous = None

        while current and current.data != key:
            previous = current
            current = current.next
        if previous is None:
            self.head = current.next
        elif current:
            previous.next = current.next
            current.next = None

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
        previous_node = None

        while current:
            next_node = current.next
            current.next = previous_node
            previous_node = current
            current = next_node
        self.head = previous_node

    def is_palindrome(self):
        """
        Check whether list is palindrome.
        :return: bool
        """
        current = self.head
        tmp = []
        while current:
            tmp.append(current.data)
            current = current.next
        return tmp == tmp[::-1]
