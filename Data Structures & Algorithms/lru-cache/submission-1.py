class Node:
    def __init__(self, key = None, val = None, prev = None, next = None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(), Node()
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node):
        node.prev = self.right.prev
        node.next = self.right
        node.prev.next = node
        self.right.prev = node
        

    def delete(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.delete(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        
        if len(self.cache) > self.capacity:
            t = self.left.next
            self.delete(t)
            del self.cache[t.key]
        


        
