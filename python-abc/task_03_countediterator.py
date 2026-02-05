#!/usr/bin/env python3


class CountedIterator:
    """Iterator wrapper that counts how many items have been retrieved."""

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """An iterator must return itself."""
        return self

    def __next__(self):
        """
        Return the next item from the iterator
        and increment the counter.
        """
        item = next(self.iterator)  # May raise StopIteration (correct behavior)
        self.count += 1
        return item

    def get_count(self):
        """Return the number of items that have been iterated over."""
        return self.count
