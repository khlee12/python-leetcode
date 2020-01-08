'''
1004. Max Consecutive Ones III
Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
Return the length of the longest (contiguous) subarray that contains only 1s. 

Example 1:
Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation: 
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

Example 2:
Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation: 
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
 
Note:
1 <= A.length <= 20000
0 <= K <= A.length
A[i] is 0 or 1 
'''
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        # sliding window-fast slow
        # increment window if satisfy
        # decrement window till satisfy & update slow
        
        slow = 0
        result = 0
        memo = [0]*2
        # print(memo)
        # if K==0, find longest substring which only has 1
        
        start = 1
        memo[0] = 1 if A[0] == 0 else 0
        
        if K==0:
            start = 0
            memo[0] = 0
        
        for fast in range(start, len(A)):
            memo[A[fast]] += 1
            if memo[0] > K:
                # not satisfy
                while memo[0] > K and slow <= fast:
                    memo[A[slow]] -= 1
                    slow += 1
            result = max(result, fast-slow+1)
            # print(memo)
        return result
