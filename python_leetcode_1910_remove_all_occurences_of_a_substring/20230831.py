s = "daabcbaabcbc" ; part = "abc"        # Output: "dab"
s = "axxxxyyyyb" ; part = "xy"           # Output: "ab"

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        ans = ""
        for ele in s:
            ans += ele
            if part == ans[-len(part):]:
                ans = ans[:-len(part)]
        return ans