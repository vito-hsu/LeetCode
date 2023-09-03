nums = [12,345,2,6,7896]    # Output: 2

class Solution:
    def findNumbers(self, nums) -> int:
        ans = 0
        for num in nums:
            if len(str(num))%2==0:
                ans+=1
        return ans