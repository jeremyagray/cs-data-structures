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

"""Record type data structures, implemented as nodes.

Record type data structures, implemented as nodes to facilitate
construction of other data strutures such as sequences and graphs.
"""


class LinkedNode:
    """A linked list node."""

    def __init__(self, record):
        """Initialize a linked list node."""
        self.record = record
        self.next = None

    def __str__(self):
        """Stringify a linked list node."""
        return str(self.record)
