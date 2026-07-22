class ListNode:
    def __init__(self, key=-1, val=-1, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}
        # linked list in order of increasing timestamps
        # the first node is the LRU, the last is the MRU
        # accessing a node moves it to the end
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        
        node = self.d[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d[key].val = value
            self.get(key)
            return
        
        if len(self.d) == self.capacity:
            # evict the first node after head
            # one node is guaranteed to exist between head and tail
            evicted_node = self.head.next
            evicted_node.prev.next = evicted_node.next
            evicted_node.next.prev = evicted_node.prev
            self.d.pop(evicted_node.key)
        
        # insert a new node before tail
        node = ListNode(key, value, None, None)
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.d[key] = node



        


        