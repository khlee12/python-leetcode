# 244. Shortest Word Distance II
# https://leetcode.com/problems/shortest-word-distance-ii/
# https://leetcode.com/problems/shortest-word-distance-ii/discuss/67028/Java-Solution-using-HashMap

class WordDistance:

    def __init__(self, words: 'List[str]'):
        self.word_pos = {}
        for i in range(len(words)):
            if words[i] in self.word_pos.keys():
                self.word_pos[words[i]].append(i)
            else:
                pos = [i]
                self.word_pos[words[i]] = pos
        
    def shortest(self, word1: 'str', word2: 'str') -> 'int':
        # 求两个数组元素的最小值
        pos1 = self.word_pos[word1]
        pos2 = self.word_pos[word2]
        g_min_distance = sys.maxsize
        i = 0
        j = 0
        while i < len(pos1) and j < len(pos2):
            if pos1[i] < pos2[j]:
                g_min_distance = min(g_min_distance, pos2[j]-pos1[i])
                i += 1
            else:
                g_min_distance = min(g_min_distance, pos1[i]-pos2[j])
                j += 1
        return g_min_distance


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
