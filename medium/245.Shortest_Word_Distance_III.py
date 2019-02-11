# 245. Shortest Word Distance III
# https://leetcode.com/problems/shortest-word-distance-iii/

class Solution:
    def shortestWordDistance(self, words: 'List[str]', word1: 'str', word2: 'str') -> 'int':
        g_min_distance = sys.maxsize
        pos1 = sys.maxsize
        pos2 = sys.maxsize
        for i in range(len(words)):
            if words[i] == word1:
                pos1 = i
            if words[i] == word2:
                if word1 == word2:
                    pos1 = pos2
                pos2 = i
            if pos1 != pos2:
                g_min_distance = min(g_min_distance, abs(pos2-pos1))
        
        return g_min_distance
