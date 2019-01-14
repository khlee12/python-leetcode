# 

class Solution:
    # def wordBreak(self, s, wordDict):
    #     """
    #     :type s: str
    #     :type wordDict: List[str]
    #     :rtype: List[str]
    #     """
#         if wordDict is None or not wordDict:
#             return []
#         if len(s) == 0:
#             return []
        
#         size = len(s)+1
#         dp = [None]*size
        
#         dp[0] = [""]
#         for i in range(1, len(s)+1):
#             temp_list = []
#             for j in range(i):
#                 if dp[j] != None and s[j:i] in wordDict:
#                     for each_element in dp[j]:
#                         space = "" if each_element == "" else " "
#                         temp_list.append(each_element + space + s[j:i])
#             dp[i] = temp_list
#         return dp[-1]
# 这个解法虽然在Solution里被推荐过，但是在以下case会出现：Memory Limit Exceeded 错误
# "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

# 以下算法通过了oj
# 先看看能不能被分割，然后再分割
# 参考：https://www.cnblogs.com/zuoyuan/p/3760804.html
    def check(self, s, dict):
        size = len(s) + 1
        dp = [False]*size
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in dict:
                    dp[i] = True
        return dp[-1]
        
    def dfs(self, s, dict, stringlist):
        if self.check(s, dict):
            if len(s) == 0: Solution.res.append(stringlist[1:])
            for i in range(1, len(s)+1):
                if s[:i] in dict:
                    self.dfs(s[i:], dict, stringlist+' '+s[:i])
    
    def wordBreak(self, s, dict):
        Solution.res = []
        self.dfs(s, dict, '')
        return Solution.res
