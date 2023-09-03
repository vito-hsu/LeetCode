nums = ["01","10"]      # Output: "11"


import itertools

class Solution:
    def findDifferentBinaryString(self, nums) -> str:
        repeat      = len(nums[0])
        key_list    = list(''.join(item) for item in itertools.product(['0','1'], repeat=repeat))
        nums        = set(nums)
        for ele in key_list:
            if ele not in nums:
                return ele

# from itertools import product
# elements = ['0', '1']
# list(''.join(item) for item in product(elements, repeat=2))
