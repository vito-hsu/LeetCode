s = "abcde" ; goal = "cdeab"    # Output: true


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s == goal:
            return True

        for _ in range(len(s)):
            s = s+s[0]
            s = s[1:]
            if s == goal:
                return True
            
        return False