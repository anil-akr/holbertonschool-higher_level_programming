#!/usr/bin/env python3


class VerboseList(list):
    """A list that prints messages whenever it is modified."""

    def append(self, item):
        """Append item to the list and print a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend list and print how many items were added."""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Remove item from list and print a notification."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop item at index (default last) and print a notification."""
        item = self[index]  # Get item before removal
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
