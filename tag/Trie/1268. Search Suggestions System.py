'''
1268. Search Suggestions System
Medium
Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.
Return list of lists of the suggested products after each character of searchWord is typed. 

Example 1:
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]

Example 2:
Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

Example 3:
Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]

Example 4:
Input: products = ["havana"], searchWord = "tatiana"
Output: [[],[],[],[],[],[],[]]
'''

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
          
        class TrieNode:
            def __init__(self):
                self.children = [None]*26
                self.isEndOfWord = False
        
        class Trie:
            def __init__(self):
                self.root = TrieNode()
            
            def insert(self, key):
                pCrawl = self.root
                length = len(key)
                for level in range(length):
                    index = ord(key[level])-ord('a')
                    # if current character is not present
                    if not pCrawl.children[index]:
                        pCrawl.children[index] = TrieNode()
                    pCrawl = pCrawl.children[index]
                
                pCrawl.isEndOfWord = True
                
            def preorder(self, node, pre, result):
                if len(result)==3:
                    return
                
                if node:
                    if node.isEndOfWord==True:
                        result.append(pre)
                    for i in range(26):
                        if not node.children[i] is None:
                            self.preorder(node.children[i], pre+chr(ord('a')+i), result)
                            
                else:
                    return []
                    
            
            def traverse(self, prefix):
                # loop till prefix
                pCrawl = self.root
                length = len(prefix)
                result = []
                flag = False
                for level in range(length):
                    temp = []
                    index = ord(prefix[level])-ord('a')
                    if flag == True:
                        result.append([])
                    else:
                        if not pCrawl.children[index]:
                            result.append([])
                            flag = True
                        else:
                            pCrawl = pCrawl.children[index]
                            self.preorder(pCrawl, prefix[:level+1], temp)
                            result.append(temp)

                return result
                
                
                
        
        root = Trie()
        for word in products:
            if word[0] == searchWord[0]:
                root.insert(word)
        
        return root.traverse(searchWord)
        
