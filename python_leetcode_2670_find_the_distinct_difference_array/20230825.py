nums = [1,2,3,4,5]      # Output: [-3,-1,1,3,5]



class Solution:
    def distinctDifferenceArray(self, nums):
        ans_list = []
        for ind, num in enumerate(nums):        # ind=0
            prefix = nums[:ind+1]
            suffix = nums[ind+1:]
            ans_list.append(len(set(prefix)) - len(set(suffix)))
        return ans_list