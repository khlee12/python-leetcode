#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 17:54:21 2018

@author: khlee
"""

#Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        result = []
        if intervals is None or not intervals:
            return result
        # sort by start
        sortedIntervals = sorted(intervals, key=lambda interval: interval.start)
        
        # loop interval list
        # init result set as first interval element 
        # if result's last element's end is bigger than next interval element
        # update end point of last element of result set
        # else append to result set
        for interval in sortedIntervals:
            if not result or result[-1].end < interval.start:
                result.append(interval)
            else:
                result[-1].end = max(result[-1].end, interval.end)
        return result

            
# 测试集        
solution = Solution()

node1 = Interval(1,3)
node2 = Interval(2,6)
node3 = Interval(8,10)
node4 = Interval(15,18)
node5 = Interval(1,4)
node6 = Interval(4,5)
node7 = Interval(2,3)
node8 = Interval(0,2)
node9 = Interval(3,5)

def printResult(result):
    for node in result:
        print(node.start, node.end)

# [[1,3],[2,6],[8,10],[15,18]]
intervalList1 = [node1, node2, node3, node4]
result1 = solution.merge(intervalList1)
printResult(result1)
# [[1,4],[4,5]]
intervalList2 = [node5, node6]
result2 = solution.merge(intervalList2)
printResult(result2)
# []
intervalList3 = []
result3 = solution.merge(intervalList3)
printResult(result3)
# None
intervalList4 = None
result4 = solution.merge(intervalList4)
printResult(result4)
# [[2,6],[1,3],[8,10],[15,18]]
intervalList5 = [node2, node1, node3, node4]
result5 = solution.merge(intervalList5)
printResult(result5)
# [[1,4],[2,3]]
intervalList6 = [node5, node7]
result6 = solution.merge(intervalList6)
printResult(result6)
# [[1,4],[0,2],[3,5]]
intervalList7 = [node5, node8, node9]
result7 = solution.merge(intervalList7)
printResult(result7)

