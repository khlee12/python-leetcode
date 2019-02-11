# 274. H-Index
# https://leetcode.com/problems/h-index/

class Solution:
    def hIndex(self, citations: 'List[int]') -> 'int':
        arr = sorted(citations)
        hIndex = len(arr)
        i = 0
        while i < len(arr) and arr[i]<hIndex:  
            hIndex -= 1
            i += 1
        return hIndex
