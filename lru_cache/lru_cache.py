from doubly_linked_list import DoublyLinkedList  # noqa: E402


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.size = 0
        self.limit = limit
        self.dll = DoublyLinkedList()
        self.storage = {}
        pass

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        # print(key)
        if key in self.storage:
            start = (self.dll.head)

            while start != None:
                if list(start.value)[0] == key:
                    self.dll.move_to_front(start)
                    break
                start = start.next

            # self.dll.move_to_front()
            return self.storage[key]
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        if key not in self.storage:

            if(self.size < self.limit):
                self.size += 1
            else:
                removed = self.dll.remove_from_tail()
                # a = list(removed.keys())
                # print("removed", (a[0]))
                self.storage.pop(list(removed.keys())[0])

            self.dll.add_to_head({key: value})
            self.storage[key] = value
        else:
            start = (self.dll.head)

            while start != None:
                if list(start.value)[0] == key:
                    self.dll.move_to_front(start)
                    break
                start = start.next

            self.storage[key] = value
            pass


lru = LRUCache(limit=3)
lru.set("aa", 1)
lru.set("bb", 1)
lru.set("cc", 2)
print(lru.set("bb", 999))
# lru.set("dd", 3)
# lru.set("ee", 5)
# lru.set("ff", 8)
# lru.set("gg", 13)

# lru.set(0, 1)
# lru.set(1, 1)
# lru.set(2, 2)
# lru.set(3, 3)
# lru.set(4, 5)
# lru.set(5, 8)
# lru.set(6, 13)

print(lru.get("ee"))
print(lru.size)
print(lru.storage)

print()
start = (lru.dll.head)
while start != None:
    print(start.value)
    start = start.next
# print(start.value)
