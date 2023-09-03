nums = [1,2,3,4]    # Output: false
nums = [3,1,4,2]    # Output: true
nums = [-1,3,2,0]   # Output: true

from scipy.stats import rankdata


class Solution:
    def find132pattern(self, nums) -> bool:
        rankdata(nums)