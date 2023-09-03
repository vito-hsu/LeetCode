words = ["pay","attention","practice","attend"] ; pref = "at"           # Output: 2
words = ["leetcode","win","loops","success"] ; pref = "code"            # Output: 0

class Solution:
    def prefixCount(self, words, pref: str) -> int:
        ans = 0
        pre_len = len(pref)
        for word in words:
            if word[:pre_len]==pref:
                ans += 1
        return ans