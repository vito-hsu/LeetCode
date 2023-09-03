secret = "1807" ; guess = "7810" # Output: "1A3B"
secret = "1123" ; guess = "0111" # Output: "1A1B"



class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        totalAB = 0
        secret1 = secret
        for guess_ele in guess:
            if guess_ele in secret1:
                secret1 = secret1.replace(guess_ele, 'a', 1)
                totalAB += 1

        totalA = 0
        for num in range(len(secret)):
            if secret[num] == guess[num]:
                totalA += 1

        return str(totalA)+'A'+str(totalAB-totalA)+'B'





