nums = [9,6,4,2,3,5,7,0,1]      # Output: 8
nums = [0,1]                    # Output: 2

class Solution:
    def missingNumber(self, nums) -> int:
        nums.sort()
        for index, num in enumerate(nums):
            # print(index, num)
            if index!=num:
                # print(index)
                return index
        return len(nums)

ans = Solution()
ans.missingNumber(nums=nums)