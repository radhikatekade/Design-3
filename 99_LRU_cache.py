# Time complexity: get - O(1), put - O(1)
# Space complexity: get - O(n), put - O(1)

# Approach - Create a doubly linked list with Head (Most recent) and Tail (Least recent). Also create 
# hashmap that has (node.key: node's reference) as (key:value) pair. 
# For get(), simply check if the key exists in hashMap, if yes, remove it from it's current ref, add it 
# to Head of LL (for most recent), and return its value, else return -1. 
# For put(), check if key exists in hashMap, if yes, do the same process as get(), else check if capacity
# is full, in which case remove the node prev to Tail of LL and delete it from hashMap. Then add the new
# node to Head of LL and hashMap.

class LRUCache:
    class Node:
        def __init__(self, key: int, value: int) -> None:
            self.key = key
            self.value = value
            self.next = None
            self.prev = None
        
    def removeNode(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def addToHead(self, node: Node) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = self.Node(-1,-1)
        self.tail = self.Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hashMap = dict()
        

    def get(self, key: int) -> int:
        if key not in self.hashMap:
            return -1
        node = self.hashMap[key]
        self.removeNode(node)
        self.addToHead(node)
        return node.value        

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            node = self.hashMap[key]
            node.value = value
            self.removeNode(node)
            self.addToHead(node)
            return
        
        if self.capacity == len(self.hashMap):
            tailPrev = self.tail.prev
            self.removeNode(tailPrev)
            del self.hashMap[tailPrev.key]
        node = self.Node(key, value)
        self.addToHead(node)
        self.hashMap[key] = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)