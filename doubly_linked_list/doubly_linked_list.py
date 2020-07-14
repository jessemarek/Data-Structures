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

        # check to see if list is empty
        if self.head is not None and self.tail is not None:
            # set head's prev to point to the new node
            self.head.prev = new_node
            # set the new node next to the head node
            new_node.next = self.head
            # change head to point to new node
            self.head = new_node
        else:
            # set the head to point to the new node
            self.head = new_node
            # set the tail to point to the new node
            self.tail = new_node

        # increase the size of the doubly linked list
        self.length += 1
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        # check to see if the head is also the tail
        if self.head.next is not None:
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

        # check to see if the list only contains 1 Node
        elif self.length == 1:
            # get reference to head
            head = self.head
            # set the list head to point to None
            self.head = None
            # set the list tail to point to None
            self.tail = None
            # decrease the size of the doubly linked list
            self.length -= 1
            # return the removed head's value
            return head.value

        else:
            return None

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        # create a new node with the value
        new_node = ListNode(value)

        if self.head is not None and self.tail is not None:
            # set the tail's next to point to the new node
            self.tail.next = new_node
            # set the new node's prev to point to the tail
            new_node.prev = self.tail
            # set the tail to point to the new_node
            self.tail = new_node
        else:
            # set the head to point to the new node
            self.head = new_node
            # set the tail to point to the new node
            self.tail = new_node

        # increase the size of the doubly linked list
        self.length += 1

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        # check to see if the head is also the tail
        if self.tail.prev is not None:
            # get a reference to the tail
            tail = self.tail
            # set the tail's next node.prev to None
            self.tail.prev.next = None
            # move the tail to the next node
            self.tail = tail.next
            # decrease the size of the doubly linked list
            self.length -= 1
            # return the value in the old tail
            return tail.value

        # check to see if the list only contains 1 Node
        elif self.length == 1:
            # get reference to tail
            tail = self.tail
            # set the list head to point to None
            self.head = None
            # set the list tail to point to None
            self.tail = None
            # decrease the size of the doubly linked list
            self.length -= 1
            # return the removed tail's value
            return tail.value

        else:
            return None

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        # get a reference to the current node
        current_node = node

        # check to see if the node is already the head
        if current_node.prev is not None:
            # set the previous node's next to the current node's next
            current_node.prev.next = current_node.next

            # check to see if current node is the tail
            if current_node.next is not None:
                # set the next node's prev to the current node's prev
                current_node.next.prev = current_node.prev

            # set the current node's prev to None
            current_node.prev = None
            # set the current node's next to the head
            current_node.next = self.head
            # change the head to point to the current node
            self.head = current_node

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
