nums = [3,6,1,0]        # Output: 1
nums = [1,2,3,4]        # Output: -1


class Solution:
    def dominantIndex(self, nums) -> int:
        max_value = max(nums)
        max_index = nums.index(max_value)
        nums2 = nums.copy()
        nums2.pop(max_index)
        if max_value>=2*max(nums2):
            return max_index
        else:
            return -1