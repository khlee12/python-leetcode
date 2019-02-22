# 228. Summary Ranges
# https://leetcode.com/problems/summary-ranges/

class Solution:
    def summaryRanges(self, nums: 'List[int]') -> 'List[str]':
        # loop each element
        # init first range as the first element
        # if current = prev+1 -> same range
        # else: end prev range, start the new range
        if not nums or nums is None:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        
        i = 1
        ranges = [str(nums[0])]
        while i < len(nums):
            if nums[i]-nums[i-1] == 1:
                if i == len(nums)-1:
                    ranges[-1] = str(ranges[-1])+'->'+str(nums[i])
                
            if nums[i]-nums[i-1] != 1:
                if ranges[-1] != str(nums[i-1]):
                    ranges[-1] = str(ranges[-1])+'->'+str(nums[i-1])
                # start new range
                ranges.append(str(nums[i]))
                
            i += 1
        return ranges
