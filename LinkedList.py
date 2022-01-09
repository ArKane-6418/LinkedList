from __future__ import annotations
from node import _Node
from typing import Any, Optional


class LinkedList:
    """A LinkedList with all the features of a typical list
    """
    _first: Optional[_Node]

    def __init__(self, head) -> None:
        """Initialize a new LinkedList
        """
        self._first = head

#    def __add__(self, other: LinkedList) -> LinkedList:
#         """Return the concatenation of two LinkedLists
#         """
#         curr = self._first
#         curr2 = other._first
#         while curr is not None or curr2 is not None:
#             if curr is not None:
#                 pass
#             elif curr2 is not None:
#                 pass
#             curr = curr.next

    def append(self, item: Any) -> None:
        """Append <item> to the LinkedList
        """
        new_node = _Node(item)
        if self._first is None:
            self._first = new_node
        else:
            curr = self._first
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    def insert(self, index: int, item: Any) -> None:
        """Insert a the given <item> at the given <index> in this LinkedList.

        Raise IndexError if index > len(self) or index < 0.
        Note that adding to the end of the list is okay.
        """
        new_node = _Node(item)
        if index == 0:
            self._first, new_node.next = new_node, self._first
        else:
            curr = self._first
            curr_index = 0
            while curr is not None and curr_index < index - 1:
                curr = curr.next
                curr_index += 1
            assert curr is None or curr_index == index - 1

            if curr is None:
                raise IndexError
            else:
                curr.next, new_node.next = new_node, curr.next

    def clear(self):
        """Clear all the nodes from the LinkedList
        """
        self._first = None

    def index(self, item: Any) -> int:
        """Return the index of the first occurrence of <item> in this list.
        """
        curr = self._first
        index = 0

        while curr is not None:
            if curr.item == item:
                return index
            index += 1
            curr = curr.next
        raise ValueError

    def count(self, item: Any) -> int:
        """Return the number of times <item> appears in the LinkedList
        """
        curr = self._first
        count = 0
        while curr is not None:
            if curr.item == item:
                count += 1
        return count

    def remove(self, item: Any) -> None:
        """Remove the first occurrence of <item> from the LinkedList
        """

        curr = self._first
        found = True
        while curr is not None and found:
            if curr.item == item:
                curr.next = curr.next.next
                found = False
            curr = curr.next

    def __delitem__(self, index: int):
        """Delete the item located at index <index>
        """
        curr_index = 0
        curr = self._first

        if index == 0:
            self._first = self._first.next
        else:
            while curr is not None and curr_index < index - 1:
                curr_index += 1
                curr = curr.next

            assert curr is None or curr_index == index - 1

            if curr is None:
                raise IndexError
            else:
                curr.next = curr.next.next

    def pop(self, index: Optional[int] = None) -> Any:
        """Remove and return the item at <index> from the LinkedList. If <index> is not provided, pop the last item
        """
        if index is None:
            popped = self.get(len(self)-1)
        popped = self.get(index)
        self.__delitem__(index)
        return popped

    def __len__(self) -> int:
        """Return the length of the LinkedList
        """
        count = 0
        if self._first is None:
            return 0
        else:
            curr = self._first
            while curr is not None:
                count += 1
                curr = curr.next
            return count

    def __str__(self) -> str:
        """Return a string representation of this LinkedList in the form
        '[item1 -> item2 -> ... -> item-n]'.
        """
        items = []
        curr = self._first
        while curr is not None:
            items.append(str(curr.item))
            curr = curr.next
        return '[' + ' -> '.join(items) + ']'

    def get(self, index: int) -> Any:
        """Return the item at position <index> in this LinkedList.

        Raise IndexError if <index> is >= the length of this list.
        """
        curr = self._first
        curr_index = 0

        while curr is not None and curr_index < index:
            curr_index += 1
            curr = curr.next

        assert curr is None or curr_index == index

        if curr is None:
            raise IndexError
        else:
            return curr.item

    def __getitem__(self, index: int) -> Any:
        return self.get(index)

    def __setitem__(self, index: int, item: Any) -> None:
        """Store item at position <index> in this LinkedList.

        Raise IndexError if index >= len(self).
        """
        curr = self._first
        curr_index = 0

        if index >= len(self):
            raise IndexError
        else:
            while curr is not None and curr_index < index:
                curr_index += 1
                curr = curr.next

            assert curr is None or curr_index == index

            if curr is None:
                raise IndexError
            else:
                curr.item = item

    def copy(self) -> LinkedList:
        """Return a copy of the original LinkedList
        """
        new = LinkedList()
        curr = self._first
        initial = _Node(curr.item)
        while curr.next is not None:
            new_node = _Node(curr.next.item)
            curr = curr.next
        new._first = initial
        return new

    def __deepcopy__(self, memodict={}):
        """Return a deepcopy of the original LinkedList
        """
        pass

    def reverse(self) -> None:
        """Reverse the LinkedList in place
        """
        curr = self._first
        prev = None
        temp_next = None

        while curr:
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next
        self._first = prev


if __name__ == "__main__":
    pass
