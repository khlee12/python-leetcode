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

# Tree
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
