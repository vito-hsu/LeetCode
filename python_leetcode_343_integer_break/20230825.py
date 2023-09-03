# n = 2               # Output: 1
# n = 10              # Output: 36
# n = 11              # 3+4+4 48
# n = 12              # 4+4+4 64
# n = 13              # 4+4+5 80
# n = 14              # 4+5+5 100
# n = 15              # 5+5+5 125
# n = 20              # Output: 625

# import math
# from functools import reduce
# from operator import mul

# class Solution:
#     def integerBreak(self, n: int) -> int:
#         key_num     = int(math.sqrt(n))
#         key_list    = [int(n/key_num)]*key_num
#         key_value   = n%key_num
#         for ind, _ in enumerate(range(key_value)):
#             key_list[ind] += 1
#         ans         = reduce(mul, key_list)
#         return ans