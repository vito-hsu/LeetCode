num = 30            # Output: 14

class Solution:
    def countEven(self, num: int) -> int:
        ans = 0
        for num in range(1, num+1):      # num = 12
            if sum([int(n) for n in list(str(num))])%2==0:
                ans += 1
        return ans