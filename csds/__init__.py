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

"""Computer science data structures suitable for instruction.

This module provides basic data structures covered during computer
science courses in high school and college, emphasizing readability
and usability for instruction.

This current includes record data as nodes, with both a ``LinkedNode``
and ``DoublyLinkedNode``, and sequences created from nodes, with a
``LinkedList``, a ``DoublyLinkedList``, and a
``CircularlyLinkedList``.
"""

from .nodes import LinkedNode
from .sequences import LinkedList
