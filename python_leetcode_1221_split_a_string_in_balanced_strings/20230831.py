s = "RLRRLLRLRL"        # Output: 4
s = "RLRRRLLRLL"        # Output: 2
s = "LLLLRRRR"          # Output: 1
s = "LL"

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        key_value = 0
        change = True
        while len(s)>0 and change:
            before_s = s
            for ind, stri in enumerate(s):
                if stri=="R":
                    key_value+=1
                else:
                    key_value-=1
                if key_value == 0:
                    ans += 1
                    s = s[ind+1:]
                    break
            if before_s == s:
                change = False
        return ans