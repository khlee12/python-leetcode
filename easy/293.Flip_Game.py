# 293. Flip Game
# https://leetcode.com/problems/flip-game/

class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        i = 0
        for i in range(1, len(s)):
            if s[i-1] == '+' and s[i] == '+':
                # flip '++' to '--'
                print(i)
                flipped = s[:i-1]+'--'+s[i+1:]
                result.append(flipped)
        return result
