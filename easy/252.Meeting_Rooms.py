# 252. Meeting Rooms
# https://leetcode.com/problems/meeting-rooms/

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def canAttendMeetings(self, intervals: 'List[Interval]') -> 'bool':
        # 按开始时间排序，如果连续两个的interval重叠-》 false
        intervals = sorted(intervals, key=lambda interval:interval.start)
        for i in range(1, len(intervals)):
            if intervals[i-1].end > intervals[i].start:
                return False
        return True
