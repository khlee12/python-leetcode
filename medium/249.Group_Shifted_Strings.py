# 249. Group Shifted Strings
# https://leetcode.com/problems/group-shifted-strings/

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = collections.defaultdict(list)
        for word in strs:
            # word to 26 sized arr
            arr = [0]*26
            for char in word:
                arr[ord(char)-ord('a')] += 1
            ans[tuple(arr)].append(word)
        return ans.values()
