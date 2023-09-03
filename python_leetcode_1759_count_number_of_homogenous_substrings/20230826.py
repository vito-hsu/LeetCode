s = "abbcccaa"  # Output: 13


class Solution:
    def countHomogenous(self, s: str) -> int:
        key_num = 0
        ans = 1
        for ind, ele in enumerate(s[1:]):
            if ele==s[ind]:
                key_num += 1
            else:
                key_num = 0
            ans += 1 + key_num
        return ans%(10**9+7)