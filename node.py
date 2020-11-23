from __future__ import annotations
from typing import Any, Optional


class _Node:
    """A Node class for a Linked List
    """
    item: Any
    next: Optional[_Node]

    def __init__(self, item: Any) -> None:
        """Initialize a new node storing <item>, with no next node.
        """
        self.item = item
        self.next = None
