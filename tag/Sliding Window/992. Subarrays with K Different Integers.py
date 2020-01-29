'''
992. Subarrays with K Different Integers
Hard
Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if the number of different integers in that subarray is exactly K.
(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)
Return the number of good subarrays of A.

Example 1:
Input: A = [1,2,1,2,3], K = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
Example 2:

Input: A = [1,2,1,3,4], K = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
 
Note:

1 <= A.length <= 20000
1 <= A[i] <= A.length
1 <= K <= A.length
'''

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        def atMost(A, K):
            left = 0
            result = 0
            nums = {}
            counter = 0
            for right in range(len(A)):
                if not A[right] in nums.keys() or nums[A[right]]==0:
                    counter+=1
                    nums[A[right]] = 1
                else:
                    nums[A[right]] += 1
                if counter <= K:
                    result += right-left+1
                else:
                    while counter > K:
                        nums[A[left]] -= 1
                        if nums[A[left]] == 0:
                            counter -= 1
                        left += 1
                    result += right-left+1
            return result
        
        return atMost(A, K)-atMost(A, K-1)
