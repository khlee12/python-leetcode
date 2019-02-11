# 134. Gas Station
# https://leetcode.com/problems/gas-station/

class Solution:
    # https://blog.csdn.net/qq508618087/article/details/50990076
    def canCompleteCircuit(self, gas: 'List[int]', cost: 'List[int]') -> 'int':
        sum_gas = 0
        sum_cost = 0
        i = 0
        start = 0
        start_log = set()
        while True:
            sum_gas += gas[i]
            sum_cost += cost[i]
            if sum_cost > sum_gas:
                start = (i+1)%(len(gas))
                if start in start_log:
                    return -1
                start_log.add(start)
                i = start
                sum_gas = 0
                sum_cost = 0
                continue
            
            i = (i+1)%(len(gas))
            if i == start:
                break
            
            
        return start
