nums = [1,2,3]  # Output: [1,3,2]
nums = [3,2,1]  # Output: [1,2,3]
nums = [1,1,5]  # Output: [1,5,1]

nums = [1,7,3,9,5,4]
nums = [1,7,3,5,9,4]
nums = [1,7,3,5,9,6,4]
nums = [1,7,3,4,9,5]
nums = [1,5,1]
nums = [1,5,5,1]
nums = [1,5,2,1]
nums = [1]
nums = [4,4,3,2,1]
nums = [2,3,1]

class Solution:
    def nextPermutation(self, nums):
        for index in range(len(nums)-1, 0, -1):     # index = 4
            key_value   = min(nums[index:])  
            if nums[index]>nums[index-1] and key_value > nums[index-1]:
                key_list    = nums[index-1:]
                key_list.remove(key_value)
                key_list.sort()
                key_list    = [key_value]+key_list
                nums[index-1:] = key_list
                return nums
            elif nums[index]>nums[index-1] and key_value < nums[index-1]:
                key_list    = nums[index-1:]
                key_value   = min([i for i in key_list if i >nums[index-1]]) # this is very important!!
                key_list.remove(key_value)
                key_list.sort()
                key_list    = [key_value]+key_list
                nums[index-1:] = key_list
                return nums
            elif nums[index]>nums[index-1] and key_value == nums[index-1]:
                key_value_l = list(set(nums[index:]))
                key_value_l.remove(key_value)
                key_value   = min(key_value_l)                              # this is also important!!
                key_list    = nums[index-1:]                               
                key_list.remove(key_value)
                key_list.sort()
                key_list    = [key_value]+key_list
                nums[index-1:] = key_list                
                return nums
            elif index==1:
                nums.sort()
                return nums

ans = Solution()
ans.nextPermutation(nums=nums)

