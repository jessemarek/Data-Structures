"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def __str__(self):
        return f"Value: {self.value}"


"""
Our doubly-linked list class. It holds references to
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        # create a new Node with the value
        new_node = ListNode(value)

        # check to see if list is empty
        if self.head is None and self.tail is None:
            # set the head to point to the new node
            self.head = new_node
            # set the tail to point to the new node
            self.tail = new_node
        else:
            # set head's prev to point to the new node
            self.head.prev = new_node
            # set the new node next to the head node
            new_node.next = self.head
            # change head to point to new node
            self.head = new_node

        # increase the size of the list
        self.length += 1
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        # delete the head node
        return self.delete(self.head)

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        # create a new node with the value
        new_node = ListNode(value)

        # check to see if list is empty
        if self.head is None and self.tail is None:
            # set the head to point to the new node
            self.head = new_node
            # set the tail to point to the new node
            self.tail = new_node
        else:
            # set the tail's next to point to the new node
            self.tail.next = new_node
            # set the new node's prev to point to the tail
            new_node.prev = self.tail
            # set the tail to point to the new_node
            self.tail = new_node

        # increase the size of the list
        self.length += 1

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        # delete the tail node
        return self.delete(self.tail)

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        # check and see if the node is already at the head and return if it is
        if node is self.head:
            return
        else:
            # delete the node
            self.delete(node)
            # create a new node at the front with the old node's value
            self.add_to_head(node.value)

    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        # check to see if node is already at the end and return if it is
        if node is self.tail:
            return
        else:
            # delete the node
            self.delete(node)
            # create a new node at the end with the old node's value
            self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the
    order of the other elements of the List.
    """

    def delete(self, node):
        # get a reference to the current node
        current = node

        # check to see if the list only contains 1 node
        if self.length == 1:
            # set the head to point to None
            self.head = None
            # set the tail to point to None
            self.tail = None
        # check to see if the node is the head
        elif current is self.head:
            # set the head to point to the current node's next
            self.head = current.next
            # set new head prev to point to None
            self.head.prev = None
        # current node must be the tail
        elif current is self.tail:
            # set the tail to point to the curret node's prev
            self.tail = current.prev
            # set new tail next to point to None
            self.tail.next = None
        # current node must be between 2 other nodes
        else:
            # set the prev node to point to the next node
            current.prev = current.next
            # set the next node to point to the prev node
            current.next = current.prev

        # decrease the length of the list
        self.length -= 1
        # return the deleted node's value
        return current.value
    """
    Finds and returns the maximum value of all the nodes
    in the List.
    """

    def get_max(self):
        # start at the head node
        current = self.head
        # init the max value to the head node's value
        max_value = current.value

        # loop through all nodes in the list and compare
        # the current value to the max value
        while current:
            # if the current value is greater replace
            # the max value with the current value
            if current.value > max_value:
                max_value = current.value
                current = current.next
            # if the current value is not greater than
            # the max value skip to next node
            else:
                current = current.next

        return max_value
