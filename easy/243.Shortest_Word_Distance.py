# 243. Shortest Word Distance
# https://leetcode.com/problems/shortest-word-distance/

class Solution:
    def shortestDistance(self, words: 'List[str]', word1: 'str', word2: 'str') -> 'int':
        min_distance = sys.maxsize
        pos1 = sys.maxsize
        pos2 = sys.maxsize
        for i in range(len(words)):
            if words[i] == word1:
                pos1 = i
            if words[i] == word2:
                pos2 = i
            if pos1 != pos2:
                min_distance = min(min_distance, abs(pos1-pos2))
        
        return min_distance
            
