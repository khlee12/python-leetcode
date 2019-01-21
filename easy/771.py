#
#

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        if J is None or not J or S is None or not S:
            return 0
        # 方法一： 用dict， 减少时间复杂度， 但是空间复杂度会增加
        # 这里用到的是这个方法
        Jewels = {}
        for i in range(len(J)):
            Jewels[J[i]] = True
        
        count = 0
        for i in range(len(S)):
            # 方法二（参考）： 全遍历， 时间复杂度会增加， 但是空间复杂度会减少
            # if S[i] in J:
            if S[i] in Jewels:
                count += 1
        
        return count
