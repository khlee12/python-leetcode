# 57. Insert Interval
# https://leetcode.com/problems/insert-interval/

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals: 'List[Interval]', newInterval: 'Interval') -> 'List[Interval]':
        
        left = []
        right = []
        s, e = newInterval.start, newInterval.end
        for each_interval in intervals:
            if newInterval.start > each_interval.end:
                left.append(each_interval)
                
            elif newInterval.end < each_interval.start:
                right.append(each_interval)
            else:
                # merge
                s = min(s, each_interval.start)
                e = max(e, each_interval.end)
        return left+[Interval(s, e)]+right
                
