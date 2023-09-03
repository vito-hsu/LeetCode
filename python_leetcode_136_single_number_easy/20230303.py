nums = [2,2,1]          # Output: 1
nums = [4,1,2,1,2]      # Output: 4
nums = [1]              # Output: 1



class Solution:
    def singleNumber(self, nums):
        for num in set(nums):
            if nums.count(num)==1:
                return num
            

########################

nums = [2,2,3,2]        # Output: 3
nums = [0,1,0,1,0,1,99] # Output: 99

class Solution:
    def singleNumber(self, nums):
        ans = 0
        for num in set(nums):
            if nums.count(num)==1:
                return num
            elif nums.count(num)==3:
                ans = num
        return ans
    
ans = Solution()
ans.singleNumber(nums=nums)