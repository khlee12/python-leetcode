# 275. H-Index II
# https://leetcode.com/problems/h-index-ii/

class Solution:
    def hIndex(self, citations: 'List[int]') -> 'int':
        hIndex = len(citations)
        i = 0
        while i < len(citations) and citations[i] < hIndex:
            hIndex -= 1
            i += 1
            
        return hIndex
