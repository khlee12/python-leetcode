# Array
## generate 2d array
```
grid = [[0 for x in range(w)] for y in range(h)]
```

## traverse 2d array by column
```
for col in list(map(list, zip(*grid))):
  # do something
```

## split string to list by each char
```
list(_str)
```

# Bit
## check each bit of an integer
```
for k in range(32):
  if ((a>>k)&1) != ((b>>k)&1):
      # different bit
      # do something
```

## Transform integer to binary string
```
binaryN = "{0:b}".format(N)
```

# Dictionary
## give the characters with count of a string
```
from collections import Counter
t = 'asjdvbaku'
_dict = Counter(t)
```
## sort by value
```
{k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
```

# Heap
## how to use max-heap?
multiply value with `-1` to invert value, and use python heapq library.

## top-k 
```
import heapq
h = []
k = 3
nums = [5,3,2,1,7,4,5]
temp_k = k+1
for i in range(len(nums)):
  if len(h) < temp_k:
      heapq.heappush(h, nums[i])
  else:
      heapq.heapreplace(h, nums[i])

topk = [x for x in reversed([heapq.heappop(h) for x in range(len(h))])][:k]
```

# Tree
## Binary Tree Depth
```
def depth(node):
    if node is None:
        return 0
    return max(depth(node.left)+depth(node.right))+1
```

## Binary Tree Every Path
```
def dfs(node, path, pathLen):
    if len(path) > pathLen:
        path[pathLen] = str(node.val)
    else:
        path.append(str(node.val))

    pathLen += 1
    if node.left is None and node.right is None:
        print(path[:pathLen]) # path from root to leaf

    left=right=None
    if node.left is not None:
        left = dfs(node.left, path, pathLen)
    if node.right is not None:
        right = dfs(node.right, path, pathLen)
```

## Trie Tree
```
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
```

# Review Problems
key point|problem url
--|--
binary tree depth+recursion|https://leetcode.com/problems/diameter-of-binary-tree/
区间内状态不变|https://leetcode.com/problems/contiguous-array/
binary search|https://leetcode.com/problems/search-in-rotated-sorted-array/
greedy algorithm|https://leetcode.com/problems/jump-game/

