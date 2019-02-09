# 299. Bulls and Cows
# https://leetcode.com/problems/bulls-and-cows/

# https://leetcode.com/problems/bulls-and-cows/discuss/74621/One-pass-Java-solution
class Solution:
    def getHint(self, secret: 'str', guess: 'str') -> 'str':
        bulls = 0
        cows = 0
        numbers = [0]*10
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                
                numbers[int(secret[i])] += 1
                numbers[int(guess[i])] -= 1
                if numbers[int(secret[i])] <= 0:
                    cows += 1
                if numbers[int(guess[i])] >= 0:
                    cows += 1
                    
        return str(bulls)+'A'+str(cows)+'B'
                
