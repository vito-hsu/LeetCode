nums = [5,2,6,1]        # Output: [2,1,1,0]
nums = [-1]             # Output: [0]
nums = [-1,-1]          # Output: [0,0]

from bisect import bisect, bisect_right, bisect_left

class Solution:
    def countSmaller(self, nums):
        ans_list = []
        key_list = []
        for num in nums[::-1]:
            key_value = bisect_left(key_list,num)
            ans_list.append(key_value)
            key_list.insert(key_value, num)
        return ans_list[::-1]



ans = Solution()
ans.countSmaller(nums=nums)