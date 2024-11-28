# ******************************************************************************
#
# cs-data-structures, simple Python data structures
#
# Copyright 2024 Jeremy A Gray <gray@flyquackswim.com>.
#
# All rights reserved.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# ******************************************************************************

"""Sequence type data structures, implemented with nodes.

Sequence type data structures, implemented with nodes to facilitate
understanding of the construction of more complex data strutures from
simpler ones.
"""


class LinkedList:
    """A linked list."""

    def __init__(self):
        """Initialize a linked list."""
        self.head = None
        self.tail = None

    def __str__(self):
        """Stringify a linked list."""
        return "[ " + ", ".join([str(n.record) for n in self]) + " ]"

    def __iter__(self):
        """Iterate over list."""
        cur = self.head

        while cur is not None:
            yield cur
            cur = cur.next

    def __len__(self):
        """Calculate the length of the linked list."""
        # Length is zero.
        if self.head is None:
            return 0

        # Length is one.
        if self.head == self.tail and self.head is not None:
            return 1

        len = 0

        cur = self.head

        while cur.next is not None:
            len += 1
            cur = cur.next

        # Count the self.tail.
        return len + 1 if len != 0 else len

    def insert_before(self, node, record=None):
        """Insert a node before another node."""
        # Prepend if no record given.
        if record is None:
            self.prepend(node)
            return

        # Create a pointer to a node and track the previous node.
        cur = self.head
        prev = None

        # Traverse the nodes until a match or the end.
        while cur is not None:
            # Check for matches.
            if cur.record == record:
                # Add the element before cur.
                if cur == self.head:
                    node.next = self.head
                    self.head = node
                else:
                    prev.next = node
                    node.next = cur

                return

            else:
                # Update the pointer and history.
                prev = cur
                cur = cur.next

    def insert_after(self, node, record=None):
        """Insert a node after another node."""
        # Append if no record given.
        if record is None:
            self.append(node)
            return

        # Current node pointer for iteration.
        cur = self.head

        # Traverse the nodes until a match or the end.
        while cur is not None:
            # Check for matches.
            if cur.record == record:
                # Add the element after cur.
                if cur == self.tail:
                    cur.next = node
                    self.tail = node
                else:
                    node.next = cur.next
                    cur.next = node

                return

            else:
                # Update the pointer and history.
                cur = cur.next

    def delete(self, record):
        """Delete a node."""
        # Empty list.
        if self.head is None:
            return None

        # Length one list.
        if len(self) == 1:
            node = self.head
            self.head = None
            self.tail = None
            return node

        # Length many list.

        # Create a pointer to a node and track the previous node.
        cur = self.head
        prev = None

        # Traverse the nodes until a match or the end.
        while cur is not None:
            # Check for matches.
            if cur.record == record:
                # Remove the element.
                if cur == self.head:
                    self.head = cur.next
                elif cur == self.tail:
                    prev.next = None
                    self.tail = prev
                else:
                    prev.next = cur.next

                return cur

            else:
                # Update the pointer and history.
                prev = cur
                cur = cur.next

    def pop(self):
        """Remove the tail node."""
        # Empty list.
        if self.head is None:
            return None

        # Non-empty list.

        # Length is one.
        if self.head == self.tail:
            node = self.head
            self.head = None
            self.tail = None
            return node

        # Length is more than one.

        # Create a pointers for iteration.
        cur = self.head
        prev = None

        # Traverse the nodes until the end.
        while cur is not None:
            if cur.next is None:
                # Dereference and return the tail node.
                prev.next = None
                self.tail = prev
                return cur
            else:
                prev = cur
                cur = cur.next

    def append(self, node):
        """Append a node to the tail."""
        # Empty list.
        if self.head is None:
            self.head = node
            self.tail = node
            return

        # Non-empty list.
        self.tail.next = node
        self.tail = node

    def prepend(self, node):
        """Prepend a node to the head."""
        # Empty list.
        if self.head is None:
            self.head = node
            self.tail = node
            return

        # Non-empty list.
        node.next = self.head
        self.head = node

    def to_gv(self):
        """Create GraphViz code for the linked list."""
        code = "strict digraph g {"
        code += 'graph [ rankdir = "LR" ];'

        cur = self.head
        i = 0

        while cur is not None:
            code += f'"node{i}" ['
            code += f'label = "<f0> record:  {str(cur.record)}| <f1> next:"'
            code += 'shape = "record"'
            code += "];"

            if cur.next is not None:
                code += f'"node{i}":f1 -> "node{i + 1}":f0 [ id = {i} ];'

            cur = cur.next
            i += 1

        code += "}"

        return code
