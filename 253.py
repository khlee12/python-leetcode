# 253. Meeting Rooms II
# https://leetcode.com/problems/meeting-rooms-ii/

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if intervals is None or not intervals:
            return 0
        
        sorted_start_time = sorted([_.start for _ in intervals])
        sorted_end_time = sorted([_.end for _ in intervals])
        
        num_rooms = 0
        end_pointer = 0
        # [[0, 30], [5, 6], [8, 20], [15, 20], [40, 50]]
        # start   0  5    8   15           40
        #  time --|--|-|--|---|--|----|----|----|---
        #   end        6         20   30        50
        #              空出来的6的房间给了8
        
        for each_start in sorted_start_time:
            if each_start < sorted_end_time[end_pointer]:
                num_rooms += 1
            else: 
                # paring end_pointer and each_start
                # 即end_pointer的空出来的会议室给了each_start
                end_pointer += 1
                
        return num_rooms
        
