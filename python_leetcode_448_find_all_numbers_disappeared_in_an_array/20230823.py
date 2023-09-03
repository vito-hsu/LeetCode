nums = [4,3,2,7,8,2,3,1]    # Output: [5,6]


class Solution:
    def findDisappearedNumbers(self, nums):
        compare_nums    = [num for num in range(1,len(nums)+1)]
        key_set         = set(nums)
        return [num for num in compare_nums if num not in key_set]