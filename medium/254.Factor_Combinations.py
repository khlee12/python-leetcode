# 254. Factor Combinations
# https://leetcode.com/problems/factor-combinations/

class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        result = []
        if n==1 or n==0:
            return result
        self.backtracking(n, result, [], 2)
        return result
    
    def backtracking(self, target, result, temp, j):
        for i in range(j, int(pow(target,1/2))+1):
            if target%i == 0:
                result.append(temp+[i, int(target/i)])
                self.backtracking(target/i, result, temp+[i], i)
