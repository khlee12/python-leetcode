# 204. Count Primes
# https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
        # https://leetcode.com/problems/count-primes/discuss/57595/Fast-Python-Solution
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                # 从i*i到n, 每隔i个设成false
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)
