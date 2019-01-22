# 146. LRU Cache
# https://leetcode.com/problems/lru-cache/

class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        # 用cache_status来存储每一次被激活的缓存的时间点
        # cache_status的value最小的，是最近没有被激活的缓存
        self.cache_data = {}
        self.cache_status = {}
        self.counter = 0
        self.capacity = capacity
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache_data.keys():
            self.cache_status[key] = self.counter
            self.counter += 1
            return self.cache_data[key]
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache_data.keys():
            self.cache_data[key] = value
        elif len(self.cache_data) == self.capacity:
            # cache is full
            not_used_key = min(self.cache_status.items(), key=lambda x:x[1])[0]
            self.cache_status.pop(not_used_key, None)
            self.cache_data.pop(not_used_key, None)
        self.cache_data[key] = value
        self.cache_status[key] = self.counter
        self.counter += 1

# 更优解
# 用Python的OrderedDict数据结构
# 将每次被激活的key放到最末尾，则dict的头就是最近没有被激活的缓存
# 还不需要额外的空间来存储被激活的status
# 参考：https://leetcode.com/problems/lru-cache/discuss/222899/simple-Python3-solution
#class LRUCache:
#
#    def __init__(self, capacity):
#        """
#        :type capacity: int
#        """
#        from collections import OrderedDict
#        self._cache = OrderedDict()
#        self._capacity = capacity
#        
#    def get(self, key):
#        """
#        :type key: int
#        :rtype: int
#        """
#        val = self._cache.get(key, -1)
#        if -1 != val:
#            self._cache.move_to_end(key)
#        
#        return val
#        
#
#    def put(self, key, value):
#        """
#        :type key: int
#        :type value: int
#        :rtype: void
#        """
#        if key in self._cache.keys():
#            self._cache.move_to_end(key)
#        else:
#            if 0 == self._capacity:
#                self._cache.popitem(last=False)
#            else:
#                self._capacity -= 1
#        self._cache[key] = value
