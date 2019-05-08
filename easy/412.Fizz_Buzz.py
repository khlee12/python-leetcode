# 412. Fizz Buzz
# https://leetcode.com/problems/fizz-buzz/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(n):
            if (i+1)%3 == 0:
                if (i+1)%5 == 0:
                    result.append('FizzBuzz')
                else:
                    result.append('Fizz')
            elif (i+1)%5 == 0:
                result.append('Buzz')
            else:
                result.append(str(i+1))
        return result
