nums = [1,2,2,4]    # Output: [2,3]
nums = [1,1]        # Output: [1,2]
nums = [2,2]        # Output: [2,1], not [1,2]


class Solution:
    def findErrorNums(self, nums):
        original_list = [num for num in range(1,len(nums)+1)]
        key_set = set(nums)
        ans_list = [num for num in original_list if nums.count(num)>1]
        ans_list.extend([num for num in original_list if num not in key_set])
        return ans_list






