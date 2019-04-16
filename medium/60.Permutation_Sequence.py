# 60. Permutation Sequence
# https://leetcode.com/problems/permutation-sequence/

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        nums = [x+1 for x in range(n)]
        k-=1
        total = 1
        factorial = [1]*n
        for i in range(2, n):
            factorial[i] = factorial[i-1]*i
            
        result = ''
        
        while nums:
            N = len(nums)-1
            index = k//(factorial[N])
            result += str(nums[index])
            del nums[index]
            k = k%(factorial[N])
            
        return result
