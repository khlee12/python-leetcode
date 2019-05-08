# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/

from heapq import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        symbolTable  = collections.Counter(nums)
        heapq = []
        for key in symbolTable:
            heappush(heapq, (-symbolTable[key], key))
        result=[]
        for i in range(k):
            result.append(heappop(heapq)[1])
        return result
