#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 15:38:50 2018

@author: khlee

https://leetcode.com/problems/fruit-into-baskets/description/
"""

class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        if tree is None or not tree:
            return 0
        
        firstPointer = 0
        secondPointer = None
        
        firstNumber = tree[firstPointer]
        secondNumber = None
        numFruits = 0
        maxNumFruits = 0
        
        for i in range(len(tree)):
            numFruits += 1
            if tree[i] != firstNumber:
                if secondNumber is None:
                    secondNumber = tree[i]
                    secondPointer = i
                    
                if tree[i] != secondNumber:          
                    firstPointer = self.updateFirstPointer(tree, i-1)
                    firstNumber = tree[firstPointer]
                    secondNumber = tree[i]
                    secondPointer = i
                    numFruits -= 1
                    
                    maxNumFruits = max(numFruits, maxNumFruits)
                    numFruits = secondPointer - firstPointer + 1
                    
        return max(numFruits, maxNumFruits)
    
    def updateFirstPointer(self, tree, pointer):
        originalNumber = tree[pointer]
        originalPointer = pointer
        i = originalPointer-1
        while i >= 0:
            if tree[i] == originalNumber:
                originalPointer -= 1
            else:
                break
            i -= 1
        return originalPointer

solution = Solution()

# 测试集
tree1 = None
tree2 = []
tree3 = [3,3,3] # 3
tree4 = [1,2,1] # 3
tree5 = [3,3,3,1,2,1,1,2,3,3,4] # 5
tree6 = [1,2,3,2,2] # 4
tree7 = [0,1,6,6,4,4,6,1] # 5
print(solution.totalFruit(tree1))
print(solution.totalFruit(tree2))
print(solution.totalFruit(tree3))
print(solution.totalFruit(tree4))
print(solution.totalFruit(tree5))
print(solution.totalFruit(tree6))
print(solution.totalFruit(tree7))

