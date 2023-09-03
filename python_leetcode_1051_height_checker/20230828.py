heights = [1,1,4,2,1,3] # Output: 3

class Solution:
    def heightChecker(self, heights) -> int:
        check_h = heights.copy()
        check_h.sort()
        ans = 0
        for ind in range(len(check_h)):
            if check_h[ind]!=heights[ind]:
                ans+=1
        return ans