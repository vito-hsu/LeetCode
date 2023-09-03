n = 886996      # Output: 0

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        key_list = list(str(n))
        ans = 0
        for ind, ele in enumerate(key_list):
            if ind%2==0:
                ans += int(ele)
            else:
                ans -= int(ele)
        return ans