# Array
## generate 2d array
```
grid = [[0 for x in range(w)] for y in range(h)]
```

# Bit
# check each bit of an integer
```
for k in range(32):
  if ((a>>k)&1) != ((b>>k)&1):
      # different bit
      # do something
```
