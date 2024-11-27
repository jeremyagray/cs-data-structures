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

"""Linked list tests."""

from csds import LinkedList
from csds import LinkedNode as Node


def test_should_append_empty_list():
    """Should append to an empty list."""
    ll = LinkedList()
    ll.append(Node(1))

    assert ll.head == ll.tail
    assert len(ll) == 1
    assert ll.head.record == 1


def test_should_append_existing_list():
    """Should append to an existing list."""
    ll = LinkedList()
    ll.append(Node(1))
    ll.append(Node(2))

    assert len(ll) == 2
    assert ll.head.next == ll.tail
    assert ll.head.record == 1
    assert ll.tail.record == 2


def test_should_pop_empty_list():
    """Should pop an empty list."""
    ll = LinkedList()
    actual = ll.pop()

    assert actual is None
    assert ll.head is None
    assert ll.tail is None
    assert ll.head == ll.tail


def test_should_pop_length_one_list():
    """Should pop a list of length one."""
    ll = LinkedList()
    expected = Node(1)
    ll.append(expected)

    actual = ll.pop()

    assert actual == expected
    assert ll.head is None
    assert ll.tail is None
    assert ll.head == ll.tail


def test_should_pop_length_many_list():
    """Should pop a list of length many."""
    ll = LinkedList()
    head = Node(1)
    expected = Node(2)
    ll.append(Node(1))
    ll.append(expected)

    actual = ll.pop()

    assert actual == expected
    assert ll.head.record == head.record
    assert ll.tail is not None
    assert ll.tail.next is None


def test_should_delete_empty_list():
    """Should delete an empty list."""
    ll = LinkedList()
    actual = ll.delete(None)

    assert actual is None
    assert len(ll) == 0
    assert ll.head is None
    assert ll.tail is None


def test_should_delete_list_length_one():
    """Should delete the item in a length one list."""
    ll = LinkedList()
    expected = Node(1)
    ll.append(expected)

    actual = ll.delete(expected.record)

    assert actual.record == expected.record
    assert len(ll) == 0
    assert ll.head is None
    assert ll.tail is None


def test_should_delete_list_length_many_head():
    """Should delete head in an existing list."""
    ll = LinkedList()
    expected = Node(1)
    ll.append(expected)
    ll.append(Node(2))
    ll.append(Node(3))

    actual = ll.delete(expected.record)

    assert actual.record == expected.record
    assert len(ll) == 2
    assert ll.head.record == 2
    assert ll.tail.record == 3
    assert ll.head.next == ll.tail


def test_should_delete_list_length_many_middle():
    """Should delete an interior element in an existing list."""
    ll = LinkedList()
    expected = Node(2)
    ll.append(Node(1))
    ll.append(expected)
    ll.append(Node(3))

    actual = ll.delete(expected.record)

    assert actual.record == expected.record
    assert len(ll) == 2
    assert ll.head.record == 1
    assert ll.tail.record == 3
    assert ll.head.next == ll.tail


def test_should_delete_list_length_many_tail():
    """Should delete tail in an existing list."""
    ll = LinkedList()
    expected = Node(3)
    ll.append(Node(1))
    ll.append(Node(2))
    ll.append(expected)

    actual = ll.delete(expected.record)

    assert actual.record == expected.record
    assert len(ll) == 2
    assert ll.head.record == 1
    assert ll.tail.record == 2
    assert ll.head.next == ll.tail


def test_should_prepend_empty_list():
    """Should prepend to an empty list."""
    ll = LinkedList()
    expected = Node(1)
    ll.prepend(expected)

    assert len(ll) == 1
    assert ll.head.record == expected.record
    assert ll.head.next is None
    assert ll.head == ll.tail


def test_should_prepend_length_one_list():
    """Should prepend to a length one list."""
    ll = LinkedList()
    ll.prepend(Node(1))
    expected = Node(0)
    ll.prepend(expected)

    assert len(ll) == 2
    assert ll.head.record == expected.record
    assert ll.head.next.record == 1
    assert ll.head.next == ll.tail


def test_should_prepend_length_many_list():
    """Should prepend to a length many list."""
    ll = LinkedList()
    ll.prepend(Node(2))
    ll.prepend(Node(1))
    expected = Node(0)
    ll.prepend(expected)

    assert len(ll) == 3
    assert ll.head.record == expected.record
    assert ll.head.next.record == 1
    assert ll.head.next.next.record == 2
    assert ll.head.next.next == ll.tail


def test_should_not_insert_before_empty_list():
    """Should not insert before on an empty list."""
    ll = LinkedList()
    ll.insert_before(Node(1), 3)

    assert len(ll) == 0
    assert ll.head is None
    assert ll.tail is None


def test_should_insert_before_empty_list():
    """Should insert before on an empty list."""
    ll = LinkedList()
    expected = Node(1)
    ll.insert_before(expected)

    assert len(ll) == 1
    assert ll.head.record == expected.record
    assert ll.head == ll.tail


def test_should_not_insert_before():
    """Should not insert before on an empty list without a match."""
    ll = LinkedList()
    head = Node(1)
    tail = Node(2)
    ll.append(head)
    ll.append(tail)
    ll.insert_before(Node(3), 3)

    assert len(ll) == 2
    assert ll.head.next == ll.tail
    assert ll.head.record == head.record
    assert ll.tail.record == tail.record


def test_should_insert_before_head_existing_list():
    """Should insert before the head on an existing list."""
    ll = LinkedList()
    target = Node(2)
    ll.append(target)
    expected = Node(1)
    ll.insert_before(expected, target.record)

    assert len(ll) == 2
    assert ll.head.record == expected.record
    assert ll.head.next.record == target.record


def test_should_insert_before_middle_existing_list():
    """Should insert before an interior element on an existing list."""
    ll = LinkedList()
    other = Node(1)
    target = Node(3)
    ll.append(other)
    ll.append(target)
    expected = Node(2)
    ll.insert_before(expected, target.record)

    assert len(ll) == 3
    assert ll.head.next.record == expected.record
    assert ll.head.next.next.record == target.record


def test_should_not_insert_after_empty_list():
    """Should not insert after on an empty list."""
    ll = LinkedList()
    ll.insert_after(Node(1), 3)

    assert len(ll) == 0
    assert ll.head is None
    assert ll.tail is None


def test_should_insert_after_empty_list():
    """Should insert after on an empty list."""
    ll = LinkedList()
    expected = Node(1)
    ll.insert_after(expected)

    assert len(ll) == 1
    assert ll.head.record == expected.record
    assert ll.head == ll.tail


def test_should_not_insert_after():
    """Should not insert after on a list without a match."""
    ll = LinkedList()
    head = Node(1)
    tail = Node(2)
    ll.append(head)
    ll.append(tail)
    ll.insert_after(Node(3), 3)

    assert len(ll) == 2
    assert ll.head.next == ll.tail
    assert ll.head.record == head.record
    assert ll.tail.record == tail.record


def test_should_insert_after_head_existing_list():
    """Should insert after the head on an existing list."""
    ll = LinkedList()
    target = Node(1)
    ll.append(target)
    expected = Node(2)
    ll.insert_after(expected, target.record)

    assert len(ll) == 2
    assert ll.head.record == target.record
    assert ll.head.next.record == expected.record


def test_should_insert_after_middle_existing_list():
    """Should insert after an interior element on an existing list."""
    ll = LinkedList()
    other = Node(1)
    target = Node(2)
    ll.append(other)
    ll.append(target)
    ll.append(Node(4))
    expected = Node(3)
    ll.insert_after(expected, target.record)

    assert len(ll) == 4
    assert ll.head.next.record == target.record
    assert ll.head.next.next.record == expected.record


def test_should_insert_after_tail_existing_list():
    """Should insert after the tail on an existing list."""
    ll = LinkedList()
    other = Node(1)
    target = Node(2)
    ll.append(other)
    ll.append(target)
    expected = Node(3)
    ll.insert_after(expected, target.record)

    assert len(ll) == 3
    assert ll.head.next.record == target.record
    assert ll.head.next.next.record == expected.record
    assert ll.tail.record == expected.record
