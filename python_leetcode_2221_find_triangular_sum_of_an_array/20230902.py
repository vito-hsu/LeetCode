nums = [1,2,3,4,5]      # Output: 8


class Solution:
    def triangularSum(self, nums) -> int:
        while len(nums)>1:
            new_nums = []
            for ind, num in enumerate(nums):
                if ind!=len(nums)-1:
                    new_nums.append((num+nums[ind+1])%10)   
            nums = new_nums.copy()
        return nums[0]