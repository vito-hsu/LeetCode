nums = [1,3,0,0,2,0,0,4]    # Output: 6
nums = [0,0,0,2,0,0]        # Output: 9


# 0     1
# 00    3
# 000   6


class Solution:
    def zeroFilledSubarray(self, nums) -> int:
        key_num = 0
        ans = 0
        for num in nums:
            if num == 0:
                ans += 1+key_num
                key_num+=1
            else:
                key_num=0
        return ans