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

from csds import LinkedNode


def test_should_stringify_linked_node():
    """Should stringify a ``LinkedNode``."""
    node = LinkedNode(1)
    actual = str(node)
    expected = "1"

    assert actual == expected
