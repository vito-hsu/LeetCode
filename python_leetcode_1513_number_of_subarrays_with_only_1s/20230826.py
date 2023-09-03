s = "0110111"       # Output: 9
s = "111111"        # Output: 21

class Solution:
    def numSub(self, s: str) -> int:
        key_num = 0
        ans     = 0
        for ind, ele in enumerate(s):
            if ele=="1":
                if ele == s[ind-1] and ind != 0:
                    key_num += 1
                    ans += key_num +1
                else:
                    ans += 1
            else:
                key_num = 0
        return ans