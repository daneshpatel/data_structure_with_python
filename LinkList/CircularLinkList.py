class Node(object):
    """
    Create Node at every call ['data' | 'next']
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


class CyclicLinkList(object):
    """
    Operations with Link list.
    """
    def __init__(self):
        self.head = None

    def __repr__(self):
        ll_list = []
        current = self.head
        if self.head is None:
            return '[]'
        ll_list.append(repr(current))
        current = current.next
        while current != self.head:
            ll_list.append(repr(current))
            current = current.next
        return '['+', '.join(ll_list)+']'

    def __len__(self):
        count = 0
        current = self.head
        if self.head is None:
            return count
        current = current.next
        count += 1
        while current != self.head:
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
            for i in range(index - 1):
                current = current.next
            current.next = Node(data=data, next=current.next)

    def append(self, data):
        """
        Data to be insert at end of list.
        :param data: Data to be insert.
        :return: None
        """
        new_node = Node(data=data)
        current = self.head
        new_node.next = new_node
        if self.head is None:
            self.head = new_node
            return
        while current.next != self.head:
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def prepend(self, data):
        """
        Data to be insert at beginning of list.
        :param data: Data to be insert.
        :return: None
        """
        current = self.head
        new_node = Node(data=data)
        new_node.next = new_node
        if self.head is None:
            self.head = new_node
            return
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head
        self.head = new_node

    def remove(self, key):
        """
        Remove the data from list
        :param key: data which will be removed
        :return: None
        """
        current = self.head
        prev = None
        if not current:
            return 'Empty List'
        if self.head.data == key:
            while current.next != self.head:
                current = current.next
            if current is self.head:
                self.head = None
                return
            current.next = self.head.next
            self.head = current.next
        else:
            while (current.data != key and
                   current.next != self.head):
                prev = current
                current = current.next
            if prev is None:
                self.head = current.next
            else:
                prev.next = current.next

    def search(self, key):
        """
        Search data in list.
        :param key: data to be searched.
        :return: obj
        """
        current = self.head
        if current is None:
            return
        while (current.data != key and
               current.next != self.head):
            current = current.next
        if current.data == key:
            return key

    def reverse(self):
        """
        Reverse the list.
        :return: None
        """
        current = self.head
        prev = None
        while current and current.next != self.head:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        if current:
            current.next = prev
            self.head.next = current
        self.head = current

    def is_palindrome(self):
        """
        Check whether list is palindrome.
        :return: bool
        """
        current = self.head
        if not current:
            return 'Empty list'
        ll_list = [current.data]
        current = current.next
        while current != self.head:
            ll_list.append(current.data)
            current = current.next
        return ll_list == ll_list[::-1]
