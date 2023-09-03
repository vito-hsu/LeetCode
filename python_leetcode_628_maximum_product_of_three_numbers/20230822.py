nums = [1,2,3]      # Output: 6
nums = [1,2,3,4]    # Output: 24
nums = [-1,-2,-3]   # Output: -6

from itertools import combinations
from functools import reduce
from operator import mul

class Solution:
    def maximumProduct(self, nums) -> int:
        if max(nums)==0:
            return 0
        elif len(nums)==3:
            return reduce(mul, nums)
        elif len(nums)==4:
            return max([reduce(mul, combo) for combo in combinations(nums, 3)])
        else:
            key_1 = max(nums)   ;   nums.remove(key_1)      # first max
            key_2 = max(nums)   ;   nums.remove(key_2)      # second max
            key_3 = max(nums)   ;   nums.remove(key_3)      # third max
            key_4 = min(nums)   ;   nums.remove(key_4)      # first min
            key_5 = min(nums)   ;   nums.remove(key_5)      # second min
            key_list = [key_1, key_2, key_3, key_4, key_5]
            return max([reduce(mul, combo) for combo in combinations(key_list, 3)])
        









from itertools import combinations

nums = [1, 2, 3, 4, 5, 6]
result = []

for combo in combinations(nums, 3):
    product = 1
    for num in combo:
        product *= num
    result.append(product)

print(result)








from itertools import combinations
from functools import reduce
from operator import mul

nums = [1, 2, 3, 4, 5, 6]
# result = [combo for combo in combinations(nums, 3)]
result = [reduce(mul, combo) for combo in combinations(nums, 3)]

print(result)