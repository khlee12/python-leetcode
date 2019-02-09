# 243. Shortest Word Distance
# https://leetcode.com/problems/shortest-word-distance/

class Solution:
    def shortestDistance(self, words: 'List[str]', word1: 'str', word2: 'str') -> 'int':
        min_distance = -1
        pos1 = -1
        pos2 = -1
        for i in range(len(words)):
            if words[i] == word1:
                pos1 = i
            if words[i] == word2:
                pos2 = i
            if pos1 != -1 and pos2 !=-1:
                if min_distance == -1:
                    min_distance = abs(pos1-pos2)
                else:
                    min_distance = min(min_distance, abs(pos1-pos2))
        
        return min_distance
            
