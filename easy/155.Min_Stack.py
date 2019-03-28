# 155. Min Stack
# https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._min = []
        self._val = []

    def push(self, x: int) -> None:
        self._val.append(x)
        if not self._min:
            self._min.append(x)
        else:
            self._min.append(min(self._min[-1], x))
        # print(self._min)
        # print(self._val)
    def pop(self) -> None:
        self._val.pop()
        self._min.pop()

    def top(self) -> int:
        return self._val[-1]

    def getMin(self) -> int:
        if self._min:
            return self._min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
