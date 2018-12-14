#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 23:23:49 2018

@author: khlee

https://leetcode.com/problems/longest-common-prefix/description/

"""

class Solution:        
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs is None or not strs:
            return ""
        if "" in strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        prefix = set(["-1"])
        
        index = -1
        min_str_len = len(strs[0])
        min_str = strs[0];
        
        for each_str in strs:
            if len(each_str) < min_str_len:
                min_str_len = len(each_str)
                min_str = each_str
        
        while len(prefix) == 1:
            index += 1
            prefix.clear();
            
            if "-1" in prefix:
                prefix.clear()
            if index > len(min_str)-1:
                break;
            
            for each_str in strs:
                prefix.add(each_str[index])
            
        return "" if index-1 < 0 else strs[0][:index]
    
solution = Solution()
test = ["aab","aab"]
print(solution.longestCommonPrefix(test))