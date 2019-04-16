# 279. Perfect Squares
# https://leetcode.com/problems/perfect-squares/

class Solution:
    _dp = [0]
    def numSquares(self, n: int) -> int:
        # classic dp
        # dp[i] = dp[j]+dp[i-j] where 1<=j<=i/2
#         dp = [sys.maxsize]*(n+1)
        
#         for i in range(1, n+1):
#             sqrt = round(pow(i, 1/2),4)
#             if sqrt*sqrt == i:
#                 dp[i] = 1
#             else:
#                 for j in range(1, i//2+1):
#                     dp[i] = min(dp[j]+dp[i-j], dp[i])
#         return dp[-1]
        
        # classic dp+math
        # dp[i] = dp[j*j]+dp[i-j*j]
#         dp = [sys.maxsize]*(n+1)
#         i = 1
#         while i*i <= n:
#             dp[i*i] = 1
#             i += 1
        
#         for i in range(1, n+1):
#             j=1
#             while i+j*j <= n:
#                 dp[i+j*j] = min(dp[i]+1, dp[i+j*j])
#                 j += 1
                
#         return dp[-1]
        # 除了这个代码，其余都出现了TLE
        dp = [0]
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]

        # dp = [0]
        # while len(dp) <= n:
        #     squares = sys.maxsize
        #     m = len(dp)
        #     for i in range(1, int(len(dp)**0.5)+1):
        #         squares = min(squares, dp[m-i*i]+1)
        #     dp.append(squares)
        # return dp[-1]
