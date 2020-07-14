"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


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

        # set head's prev to point to the new node
        self.head.prev = new_node

        # set the new node next to the head node
        new_node.next = self.head

        # change head to point to new node
        self.head = new_node

        # increase the size of the doubly linked list
        self.size += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        # get a reference to the head
        head = self.head

        # set the head's next node.prev to None
        self.head.next.prev = None

        # move the head to the next node
        self.head = head.next

        # decrease the size of the doubly linked list
        self.length -= 1

        # return the value in the old head
        return head.value

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        # create a new node with the value
        new_node = ListNode(value)

        # set the tail's next to point to the new node
        self.tail.next = new_node

        # set the new node's prev to point to the tail
        new_node.prev = self.tail

        # set the tail to point to the new_node
        self.tail = new_node

        # increase the size of the doubly linked list
        self.length += 1

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        # get a reference to the tail
        tail = self.tail

        # set the tail's prev node.next to point to None
        self.tail.prev.next = None

        # move the tail reference to point at the new tail node
        self.tail = tail.prev

        # decrease the size of the doubly linked list
        self.length -= 1

        # return the value from the old tail
        return tail

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        pass

    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the
    order of the other elements of the List.
    """

    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes
    in the List.
    """

    def get_max(self):
        pass
