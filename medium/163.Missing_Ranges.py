# 163. Missing Ranges
# https://leetcode.com/problems/missing-ranges/

class Solution:
    def findMissingRanges(self, nums: 'List[int]', lower: 'int', upper: 'int') -> 'List[str]':
        # loop each element
        # if current-1 == prev -> same range
        # else: start a new range as [prev, current]
        if upper < lower:
            return []
        if not nums or nums is None:
            return [str(lower)+'->'+str(upper)] if lower != upper else [str(upper)]
        
        nums.append(upper+1)
        pre = lower-1
        ranges = []
        for curr in nums:
            if curr-pre == 2:
                ranges.append(str(curr-1))
            elif curr > pre+2:
                ranges.append(str(pre+1)+'->'+str(curr-1))
            pre = curr
        
        return ranges
