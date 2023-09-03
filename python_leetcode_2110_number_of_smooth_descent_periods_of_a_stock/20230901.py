prices = [3,2,1,4]      # Output: 7
prices = [8,6,7,7]      # 4


class Solution:
    def getDescentPeriods(self, prices) -> int:
        ans = 0
        key_value = 0
        for ind, price in enumerate(prices):
            if ind == 0:
                ans += 1
            else:
                if price+1==prices[ind-1]:
                    key_value += 1
                    ans += key_value +1
                else:
                    key_value = 0
                    ans += 1
        return ans