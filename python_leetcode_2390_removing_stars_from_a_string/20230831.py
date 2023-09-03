s = "leet**cod*e"       # Output: "lecoe"

class Solution:
    def removeStars(self, s: str) -> str:
        ans = ""
        for ele in s:
            if ele == "*":
                ans = ans[:-1]
            else:
                ans += ele
        return ans