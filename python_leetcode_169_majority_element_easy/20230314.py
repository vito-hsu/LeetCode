nums = [3,3,4]  # 3


class Solution:
    def majorityElement(self, nums) -> int:
        key_list = set(nums)
        for i in key_list:
            if nums.count(i)>=len(nums)*0.5:
                return i
            

ans = Solution()
ans.majorityElement(nums=nums)