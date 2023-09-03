nums = [4,3,6,16,8,2]           # Output: 3
nums = [2,3,5,6,7]              # Output: -1




class Solution:
    def longestSquareStreak(self, nums) -> int:
        nums = list(set(nums))
        nums.sort()
        
        key_set = set(nums)
        
        ans_list = []

        for num in nums:
            ans = 1
            value = num
            while value**2 in key_set:
                ans += 1
                value = value**2
            ans_list.append(ans)

        if max(ans_list)==1:
            return -1
        else:
            return max(ans_list)
