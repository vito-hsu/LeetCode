nums = [1,13,10,12,31]      # Output: 6

class Solution:
    def countDistinctIntegers(self, nums) -> int:
        key_set = {num for num in set(nums)}
        ans = len(key_set)
        for num in nums:
            if int(str(num)[::-1]) not in key_set:
                ans += 1
                key_set.add(int(str(num)[::-1]))
        return ans