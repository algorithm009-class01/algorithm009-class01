class MyCircularDeque:
    """
    self.front is the index before the start of the queue
    self.last is the index after the end of the queue
    Example:
        For queue sequence [1, 2, 3, 4, 5, 6], index (0, 1, 2, 3, 4, 5)
    self.front = 5, self.last = 1
        For queue sequence [4, 5, 6, 1, 2, 3], index (0, 1, 2, 3, 4, 5)
    start of the queue is element 1, index 3
    end of the queue is element 6, index 2
    self.front = 2
    self.last = 3
    """

    def __init__(self, k):
        """Initialize your data structure here. Set the size of deque to be k."""
        self.capacity = k
        self.deque = [0] * k    # [0, 0, 0, .. 0]
        self.size = 0
        self.front = (k-1) % k  # Point to the end of the list
        self.last = 0           # Point to the front of the list

    def insertFront(self, value: int) -> bool:
        """Adds an item at the front of deque. Return true if the operation is successful"""
        if self.size+1 <= self.capacity:
            self.deque[self.front] = value
            self.front = (self.front - 1) % self.capacity
            self.size += 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        """Adds an value at the rear of Deque. Return true if the operation is successful"""
        if self.size+1 <= self.capacity:
            self.deque[self.last] = value
            self.last = (self.last + 1) % self.capacity
            self.size += 1
            return True
        return False

    def deleteFront(self) -> bool:
        """Deletes an item from the front of Deque. Return true if the operation is successful."""
        if self.size > 0:
            self.deque[(self.front + 1) % self.capacity] = None
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
            return True
        return False

    def deleteLast(self) -> bool:
        """Deletes an item from the rear of Deque. Return true of the operation is successful"""
        if self.size > 0:
            self.deque[(self.last-1) % self.capacity] = None
            self.last = (self.last-1) % self.capacity
            self.size -= 1
            return True
        return False

    def getFront(self) -> int:
        """Get the front item from the queue."""
        if self.size > 0:
            return self.deque[(self.front + 1) % self.capacity]
        return -1

    def getRear(self) -> int:
        """Get the last item from the deque."""
        if self.size > 0:
            return self.deque[(self.last-1) % self.capacity]
        return -1

    def isEmpty(self) -> bool:
        """Checks whether the circular deque is empty or not."""
        return self.size == 0

    def isFull(self) -> bool:
        """Checks whether the cirtular deque if full or not"""
        return  self.size == self.capacity


obj = MyCircularDeque(3)
param_1 = obj.insertFront(3)
param_2 = obj.insertLast(2)
param_3 = obj.deleteFront()
param_4 = obj.deleteLast()
param_5 = obj.getFront()
param_6 = obj.getRear()
param_7 = obj.isEmpty()
param_8 = obj.isFull()