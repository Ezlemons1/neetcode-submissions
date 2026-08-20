class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        previous, nextnode = node.prev, node.next
        previous.next, nextnode.prev = nextnode, previous
        # the process is: instantiate two new variables, one pointing to the node prev and one pointing to the node next. then, make them skip over the current node: previous.next = nextnode, nextnode.prev = previous
    
    def insert(self, node):
        previous, nextnode = self.right.prev, self.right
        previous.next = nextnode.prev = node
        node.next, node.prev = nextnode, previous
        # a little easier than remove, the process is: instantiate the same two new variables, set them equal to the previous node from right and the rightmost node. then, have the previous node point to new node, have rightmost node point prev to the new node, then assign the new node next and prev pointers

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
            # remove, then insert again as we are implementing a lru cache, the most recently used should be on the rightmost side
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
