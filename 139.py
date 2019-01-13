# 139. Word Break
# https://leetcode.com/problems/word-break/

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if wordDict is None or not wordDict:
            return False
        if len(s) == 0:
            return False
        
        size = len(s)+1
        dp = [False]*size
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] == True and s[j:i] in wordDict:
                    dp[i] = True
                    break
        
        return dp[-1]
