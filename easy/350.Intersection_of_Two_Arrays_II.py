# 350. Intersection of Two Arrays II
# https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        N1 = len(nums1)
        N2 = len(nums2)
        
        def buildSymbolTable(nums):
            result = collections.defaultdict(list)
            for i in range(len(nums)):
                if not nums[i] in result:
                    result[nums[i]] = [i]
                else:
                    result[nums[i]].append(i)
            return result
        
        N = N1
        base = nums1
        compared = buildSymbolTable(nums2)
        if N1 < N2:
            N = N2
            base = nums2
            compared = buildSymbolTable(nums1)
        
        result = []
        for i in range(N):
            if base[i] in compared:
                indexes = compared[base[i]]
                if len(indexes) >=1:
                    result.append(base[i])
                    compared[base[i]].pop(0)
                    
        return result
                
