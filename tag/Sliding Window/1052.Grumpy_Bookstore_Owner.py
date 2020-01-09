'''
1052. Grumpy Bookstore Owner
Today, the bookstore owner has a store open for customers.length minutes.  Every minute, some number of customers (customers[i]) enter the store, and all those customers leave after the end of that minute.
On some minutes, the bookstore owner is grumpy.  If the bookstore owner is grumpy on the i-th minute, grumpy[i] = 1, otherwise grumpy[i] = 0.  When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise they are satisfied.
The bookstore owner knows a secret technique to keep themselves not grumpy for X minutes straight, but can only use it once.
Return the maximum number of customers that can be satisfied throughout the day.

Example 1:

Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.

Note:
1 <= X <= customers.length == grumpy.length <= 20000
0 <= customers[i] <= 1000
0 <= grumpy[i] <= 1
'''
# Certain Window Size Sliding Window + Prefix Sum
# with support array

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        # certain size of window
        sum_at_minute = [0]*len(customers)
        sum_at_minute[0] = customers[0] if grumpy[0] == 0 else 0
        for i in range(1, len(customers)):
            if grumpy[i]==0:
                sum_at_minute[i] = sum_at_minute[i-1]+customers[i]
            else:
                sum_at_minute[i] = sum_at_minute[i-1]
        
        result = 0
        for i in range(len(customers)-X+1):
            temp_sum = sum(customers[i:i+X])
            
            if i==0:
                temp_sum += sum_at_minute[-1]-sum_at_minute[i+X-1]
            elif i==len(customers)-X:
                temp_sum += sum_at_minute[i-1]
            else:
                temp_sum += sum_at_minute[i-1]+(sum_at_minute[-1]-sum_at_minute[i+X-1])
            # print(temp_sum)
                
            result = max(result, temp_sum)
        
        return result
