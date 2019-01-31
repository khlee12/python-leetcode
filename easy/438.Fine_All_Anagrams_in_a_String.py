# 438. Find All Anagrams in a String
# https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        pattern_len = len(p)
        result = []
        word1_dict = collections.Counter()
        word2_dict = collections.Counter(p)
    
        # 遍历字符串，找到anagram，将pos放入结果数组中
        for i in range(len(s)-pattern_len+1):
            # slicing
            sliced = s[i:i+pattern_len]
            word1_dict = collections.Counter(sliced)
            if word1_dict == word2_dict:
                result.append(i)

        return result
    

        
