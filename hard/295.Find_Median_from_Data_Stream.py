# 295. Find Median from Data Stream
# https://leetcode.com/problems/find-median-from-data-stream/

from heapq import *
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        使用Python的内置堆算法heapq可以很容易地实现小顶堆，而大顶堆可以通过对元素的值 * -1实现。
        需要满足下面的约束条件：
            大顶堆中存储的元素 均不大于 小顶堆中的元素
            MaxHeap.size() == MinHeap.size()，或者 MaxHeap.size() == MinHeap.size() + 1
        则有：
            当MaxHeap.size() == MinHeap.size() + 1时，中位数就是MaxHeap的堆顶元素
            当MaxHeap.size() == MinHeap.size()时，中位数就是MaxHeap堆顶元素与MinHeap堆顶元素的均值
        http://bookshadow.com/weblog/2015/10/19/leetcode-find-median-data-stream/
        """
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heappush(self.maxHeap, -num)
        minTop = self.minHeap[0] if len(self.minHeap) else None
        maxTop = self.maxHeap[0] if len(self.maxHeap) else None
        if (minTop and maxTop and (minTop < -maxTop)) or len(self.minHeap)+1 < len(self.maxHeap): 
            # balance数组大小， 使minHeap和maxHeap的大小差为1
            heappush(self.minHeap, -heappop(self.maxHeap))
        if len(self.maxHeap) < len(self.minHeap): # 保证中间值是maxHeap的top
            heappush(self.maxHeap, -heappop(self.minHeap))
        # print(self.maxHeap)
        # print(self.minHeap)
    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -1*self.maxHeap[0]
        return (-1*self.maxHeap[0]+self.minHeap[0])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
