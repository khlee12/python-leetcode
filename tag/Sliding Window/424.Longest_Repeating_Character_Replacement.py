'''
424. Longest Repeating Character Replacement
Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.
In one operation, you can choose any character of the string and change it to any other uppercase English character.
Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:
Input:
s = "ABAB", k = 2
Output:
4
Explanation:
Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input:
s = "AABABBA", k = 1
Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # find window satisfy
        # 1) longest sub string
        # 2) len(substring)-max(count(unique letter)) <= k

        slow = 0
        _map = {}
        result = 0
        
        for fast in range(len(s)):
            if not s[fast] in _map.keys():
                # not exist
                _map[s[fast]] = 1
            else:
                # exist
                _map[s[fast]] += 1
            
            # check if satisfy
            if (fast-slow)+1-max(_map.values()) > k:
                # not satisfy
                while slow < fast and (fast-slow)+1-max(_map.values()) > k:
                    # update slow
                    _map[s[slow]] -= 1
                    slow += 1
                    
            # else: 
            #   # not satisfy
            #   # fast + 1
            result = max(result, fast-slow+1)
        return result
