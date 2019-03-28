# 232. Implement Queue using Stacks
# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    class MyStack:
        def __init__(self):
            self.val = []
        def push(self, x):
            # print('hssss')
            self.val.append(x)
        def pop(self):
            if self.val:
                return self.val.pop()
        def top(self):
            return self.val[-1]
        def empty(self):
            if len(self.val) <= 0:
                return True
            return False
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val1 = self.MyStack()
        self.val2 = self.MyStack()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if not self.val2.empty():
            while True:
                if self.val2.empty():
                    break
                temp = self.val2.pop()
                self.val1.push(temp)
        self.val1.push(x)
        
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.val2.empty():
            while True:
                if self.val1.empty():
                    break
                temp = self.val1.pop()
                
                self.val2.push(temp)
        if self.val2.empty():
            return None
        return self.val2.pop()
        
    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.val2.empty():
            return self.val2.top()
        while True:
            if self.val1.empty():
                break
            temp = self.val1.pop()
            self.val2.push(temp)
        if self.val2.empty():
            return None
        return self.val2.top()
        
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.val1.empty() and self.val2.empty():
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
